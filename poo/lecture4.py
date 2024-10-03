class Banco:
    def __init__(self,name,lastname,cui,acount,amount):
        """ funcion inicializadora
        Argumentos:
        name(string):nombre del usuario
        lastname(string):apellido del usuario
        cui(int):numero de identificacion dni
        acount(int):numero de cuenta
        amount(int):saldo o monto del usuario
        """
        
        self.name=name
        self.lastname=lastname
        self.cui=cui
        self.acount=acount
        self.amount=amount
    def deposit(self,amount):
        self.amount+=amount
        
    def remove_cash(self,amount):
        if amount > self.amount:
            return "no cuentas con saldo suficiente"
        self.amount-=amount
        
    def status_acount(self):
        response=f"""
        ------BIENVENIDO AL BANCO "TEPINCHA Y ESTAFA"------
        Cliente: {self.name}, {self.lastname}  NroCuenta:{self.acount}.
        En estos momentos tienes un saldo de : s/.{self.amount},
        fin del voucher:
        ___________________________________________________________________
        """
        return response

cliente_miguel=Banco("Miguelito","Barraza",784512963,4545,30)
print(cliente_miguel.status_acount())
cliente_miguel.deposit(100)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
`