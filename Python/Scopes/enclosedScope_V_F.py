def parent():
    pName="srinu" #local #elcosed varaible

    def child():
        cName="vamsi" # local # enclosed 
        print(cName)
        print(pName)

        def nestedChild():
            nName="xyz" #local var
            print(cName)
            print(pName)

        # nestedChild()
    nestedChild()

    print(pName)
    child()  
parent()

# global  # global :-- local :-- global varaible local modify
# non-local # nested child :-- 