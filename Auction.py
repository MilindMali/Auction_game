 
bids={}
end=True

while end:

  username=input("what is name of user ?\n")
  bid_price=int(input("what is bidding price ?\n"))
  
  bids[username]=bid_price

  another_user=input("is there anyone who want to bid ?\n")

  if another_user=='yes':
    bids[username]=bid_price
  elif another_user=='no':
    end=False

winer=max(bids, key=bids.get)

print(f'The bid winner is {winer} and bidding price is {bids[winer]}')