from fractions import Fraction as F

class DL(list):
    """Représentation d'un DL en 0 sous forme de liste où les x sont rangés par degrés croissants

    Attributs:
        DL (list): coefficients du DL
        ordre (int): ordre du DL
    """
    def __init__(self, DL):
        """Le constructeur de la classe DL

        Args:
            DL (list(str)): coefficients du DL
        """
        super().__init__()
        self.DL = []
        for element in DL:
            if isinstance(element,str):
                i = element.split("/")
                if len(i) == 1:
                    self.DL.append(
                        F(int(i[0]))
                        )
                else : 
                    self.DL.append(
                        F(int(i[0]), int(i[1]))
                        )
            else:
                self.DL.append(element)
        self.ordre = len(DL)
        
    def plus(self, Q):
        """Permet de faire la somme de 2 DL en 0 donnés en entrée sous forme de liste.
        L'ordre du DL renvoyé sera le plus petit entre self et Q.

        Args:
            Q (DL): DL à ajouter à self

        Returns:
            DL: somme de self et Q. 
        """
        n = min(self.ordre, Q.ordre)
        return DL([self.DL[i] + Q.DL[i] for i in range(n)])
    
    def fois(self, Q):
        """Permet de faire le produit de 2 DL en 0 donnés en entrée sous forme de liste.
        L'ordre du DL renvoyé sera le plus petit entre self et Q.

        Args:
            Q (DL): DL à multiplier à self

        Returns:
            DL: produit de self et Q. 
        """
        n = min(self.ordre, Q.ordre)
        result = []
        for k in range(n):
            s = 0
            for l in range(k+1):
                s+= self.DL[l] * Q.DL[k-l] # x^l * x^(k-l) = x^k
            result.append(s)
        return DL(result)
        
        
    def scalaire(self,a):
        """Multiplie un DL par un scalaire

        Args:
            a (float): le scalaire
        """
        return DL([a*element for element in self.DL])
    
    def puissance(self,n):
        """Renvoie le DL a une certaine puissance

        Args:
            n (int): puissance
            
        Returns:
            DL
        """
        if n == 0:
            return DL(["1"])
        elif n == 1:
            return self
        else :
            return self.fois(self.puissance(n-1))
        
    def inversed(self):
        """Renvoie l'inverse du DL en passant par 1/(1+u) avec self ne s'annulant pas en 0"""
        coef = self.DL[0]
        P = DL(self.DL)
        P.DL[0] = F(0)
        P.scalaire(1/coef)
        result = DL([1]+[0]*(self.ordre-1))
        for i in range(1,P.ordre):
            result = result.plus(
                P.scalaire((-1)**i).puissance(i)
                )
        return result.scalaire(coef)
            
    def sur(self,Q):
        """Renvoie le DL de self sur Q

        Args:
            Q (DL)
        """
        return self.fois(Q.inversed())
    
    
    def __str__(self) -> str:
        result = ""
        for i,element in enumerate(self.DL):
            if element != 0:
                if i == 0:
                    result += element.__str__() + " "
                elif element >0:
                    result += "+"+element.__str__() + f'*x^{i} '
                else :
                    result += element.__str__() + f'*x^{i} '
        return str(result)
        

if __name__=="__main__":
    DL4_exp = DL(["1", "1", "1/2", "1/6", "1/24"])
    DL4_cos = DL(["1", "0", "-1/2", "0", "1/24"])
    exp_cos= DL4_exp.plus(DL4_cos)
    print(f"e^x + cos(x)= {exp_cos}")
    DL4_ln = DL(["0","1","-1/2","1/3","-1/4"])
    DL4_sh = DL(["0","1","0","1/6","0"])
    P = DL4_ln.fois(DL4_sh)
    print(f"ln(1+x)*sh(x) = {P}")
    print(f"2*ln(1+x)*sh(x) = {P.scalaire(2)}")
    print(f"(e^x + cos(x))^3 = {exp_cos.puissance(3)}")
    print(f"1/cos(x) = {DL4_cos.inversed()}")
    print(f"e^x / cos(x) = {DL4_exp.sur(DL4_cos)}")    