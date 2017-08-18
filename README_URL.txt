/promotions/api/			#Get all the active promotion banners based on the logic dateFr<=Todat<=dateTo.
/merchants/api/				#Get all the merchants.
/merchants/api/?search=roti		#Search all the merchants which names contains "roti"
/merchants/api/1/			#Get one particular detail for merchant with id =1
/users/api/login/			#Obtain jwt with parameter {username="", password=""}
/users/api/register/			#Registration for users which accepts json data {username="",email1="",email2="",password=""}
/users/api/<username>/			#Get the profile detail of that username with jwt parameter {Authorization JWT <token ID>}
/cards/api/				#Get the list of all cards under the authenticated username.
/cards/api/<id>/			#Get the detail of the card
/cards/api/<id>/edit			#Update the detail of the card
/cards/api/<id>/delete			#delete the card
/transactions/api/			#Get the list of all transactions under authenticated username ordererd by latest transaction.
/transactions/api/ios-20170801-000000/	#Get the detail of a particular transaction.