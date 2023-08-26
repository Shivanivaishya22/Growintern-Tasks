from django.shortcuts import render , redirect
from Admin.models import Category,Product,User,MyCart,WishList, Payment, Orders , Address
from django.contrib import messages

# Create your views here.
def home(request):
    cats = Category.objects.all()
    prod = Product.objects.all()
    return render (request ,"home.html", {"cats":cats,"prod":prod})

def Login(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request, "Login.html" , {"cats":cats })
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            #if user already exists
            user = User.objects.get(usernm=uname)
            print(user)
        except:
            #loginfailed
            messages.info(request, "Invalid Username")
            return render(request,"Login.html", {"cats":cats})
        else:
            if(user.password == pwd):

            #if login is successful then we create a session 
                 request.session["uname"] = uname
            # messages.info(request, "Congratulations , Your log in is successful...")
                 return redirect(home)
            else:
                
                  messages.info(request, "Password is incorrect.")
                  return redirect(home) 

def Signup(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request, "signup.html" , {"cats":cats })
    else:
        fname = request.POST["fname"]        
        uname = request.POST["uname"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        adrs = request.POST["adrs"]
        pwd = request.POST["pwd"]
        try:
            #is user already present
            user = User.objects.get(usernm = uname)
        except:
            #we can create user , as user is not present
            user = User()
            user.fullname = fname
            user.usernm = uname
            user.email = email
            user.contact = contact
            user.address = adrs
            user.password = pwd
            user.save()
            messages.info(request, "Successful Sign In , Please Login Now")
            return redirect(Login)
        else:
            
            # messages.info(request, "Sorry , This User Already Exist . Please Login First")
            return render(request , "signup.html", {"cats":cats})

def SignOut(request):
    # delete the session
    request.session.clear()
    return redirect(home)       
def showproducts(request , id):
    Cats = Category.objects.all()
    prod = Product.objects.filter(category = id)
    return render(request , "products.html" ,{"cats":Cats , "prod": prod} )

def addToCart(request):
    cats = Category.objects.all()
    prod = Product.objects.all()
    if("uname" in request.session):   #check user has logged in
        #get userinfo
        user = User.objects.get(usernm = request.session["uname"])
        # get the product information
        prod_id = request.POST["pid"]
        prodct = Product.objects.get(id = prod_id)
        qty = request.POST["qty"]
        action = request.POST["action"]
        if(action == "addtocart"):
            try:
                item = MyCart.objects.get(user=user, prodct=prodct)
            except:
                cart = MyCart()
                cart.user = user
                cart.prodct = prodct
                cart.qty = qty
                cart.save()
                messages.info(request, "Item added successfully...")
            else:
            #return HttpResponse("Item already in cart")
                messages.info(request, 'Item already in the cart..')
            return redirect(ShowCart)
        else:
            try:
                item = WishList.objects.get(user=user,prodct=prodct)
            except:
                listt = WishList()
                listt.user = user
                listt.prodct = prodct
                listt.qty = qty
                listt.save()
                messages.info(request, "Item added to the wishlist...")
            else:                
                messages.info(request, 'Item already in wishlist...')
            return redirect(WishItem)
    else:
        messages.error(request , "Please Login Here...")
        return redirect(Login)

def Viewdetails(request , id):
    cats = Category.objects.all()
    prod = Product.objects.get(id=id)
    return render(request , "viewdetails.html" , {"cats":cats, "prod":prod})

def ShowCart(request):
    cats = Category.objects.all()
    prod = Product.objects.all()
    if(request.method == "GET"):
        user = User.objects.get(usernm = request.session["uname"] )
        items = MyCart.objects.filter(user = user)
        print(items)
        subtotal = 0
        total = 0
        for item in items:
            subtotal += item.qty * item.prodct.price
        request.session["subtotal"] = subtotal
        total = subtotal + 100
        request.session["total"] = total
        return render (request, "Showcart.html", {"items":items,"total":total,"cats":cats,"prod":prod})
    else :
        cart_id = request.POST["cart_id"]
        item = MyCart.objects.get(id=cart_id)
        action = request.POST["action"]
        if(action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        return redirect(ShowCart) 

def WishItem(request):
    cats = Category.objects.all()
    prod = Product.objects.all()
    if(request.method == "GET"):
        items = WishList.objects.filter(user = request.session["uname"])          
        return render (request , "wishitem.html" , {"items": items,"cats":cats,"prod":prod})
    else :
        cart_id = request.POST["cart_id"]
        item = WishList.objects.get(id=cart_id)
        action = request.POST["action"]
        
        if(action == "remove"):
            item.delete()
            return redirect(WishItem)
        else:
             #get userinfo
            user = User.objects.get(usernm = request.session["uname"])
            # get the art information
            prod = Product.objects.get(id = cart_id)
            qty = request.POST["qty"]
            action = request.POST["action"]
            try:
                item = MyCart.objects.get(user=user,prod=prod)
            except:
                cart = MyCart()
                cart.user = user
                cart.prodct = prod
                cart.qty = qty
                cart.save()
                messages.info(request, "Item added successfully in wishlist...")
                item.delete()
            else:
            #return HttpResponse("Item already in cart")
                messages.info(request, 'Item already in cart')
            return redirect(ShowCart)
            
def aboutus(request):
    cats = Category.objects.all()
    prod = Product.objects.all()
    return render(request , "about.html" , {"cats":cats, "prod":prod})

def makePayment(request):
    if (request.method == "GET"):
        return render(request , "makepayment.html", {})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
        except:
            return redirect(makePayment)
        else:
            owner = Payment.objects.get(card_no='222', cvv='222' ,expiry='12/2025')
            print(request.session["total"])
            buyer.balance -= float(request.session["total"])
            owner.balance += float(request.session["total"])
            buyer.save()
            owner.save()

            myorder = Orders()
            user = User.objects.get(usernm=request.session["uname"])
            myorder.user  = user
            myorder.amount = request.session["total"]
            items = MyCart.objects.filter(user=user)
            details = ""
            for item in items:
                details+= item.prodct.pname+" "
                item.delete()

            myorder.details= details
            myorder.save()
            messages.info(request, "Order Confirmed!! Thank You For Your Visit...")

            #delete all cart items
            return redirect(home)
        
def address(request):
    cats = Category.objects.all()
    prod = Product.objects.all()
    if(request.method == "GET"):
 
        return render(request, "address.html" , {"cats":cats , "prod": prod})
    else:        # if("uname" in request.session):   #check user has logged in
        namee = request.POST["namee"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        add = request.POST["add"]
        town = request.POST["town"]
        city = request.POST["city"]
        adrs = Address()

        adrs.name = namee
        adrs.email=email
        adrs.contact=contact
        adrs.add=add
        adrs.town=town
        adrs.city=city
        adrs.save()
        return redirect(makePayment)
