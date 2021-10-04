import PracticeClass as pc

def main():
    dict = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
    }


    num = dict["medical"][0]["room-number"]
    use = dict["medical"][0]["use"]
    size = dict["medical"][0]["sq-ft"]
    price = dict["medical"][0]["price"]

    room = pc.Practice(num,use,size,price)

    print(room.get_room_number())
    print(room.get_room_use())
    print(room.get_room_size())
    print(format(room.price_per_sqft(size,price),'.2'))



main()