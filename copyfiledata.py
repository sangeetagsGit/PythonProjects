# Copy data from one file to another

with open("aq1.txt","r+") as f:
    data=f.read()
    print(data)
    f.write(data+"\nNew data added")