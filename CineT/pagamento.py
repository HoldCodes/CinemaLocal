from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os , sys
import tempfile
import janelas
from main import Carrinho

"""
    Apenas a tela de pagamento e as funcionalidades de add/remover produtos e emitir nota fiscal foram implementas
    - falta 
        - pegar informação do banco de dados
        - integrar informações entre demais telas
        - tirar os produtos do banco de dados
    
"""


class Store:
    def __init__(self,window, carrinho):
        window.destroy()
        self.win = window
        self.carrinho = carrinho
        self.win = Tk()
        self.win.geometry("900x685")
        
        #centraliza janela
        self.win.geometry(f"+{int((self.win.winfo_screenwidth() / 2) - (900 / 2))}+"f"{int((self.win.winfo_screenheight() / 2) - (685 / 2))}")

        #produtos
        self.categories=["Ingresso", "Pipoca","Bebida"]

        self.Ingresso=["INGRESSO 2D - Intei.","INGRESSO 2D - Meia", "INGRESSO 3D - Intei.", "INGRESSO 2D - Meia"]
        self.Pipoca=["Pipoca - Doce media  ","Pipoca - Sal. media"]
        self.Bebida=["Refrigerante 300ml","Suco 250ml"]

        #Variaveis
        self.cname=StringVar()
        self.cmob=StringVar()
        self.cbill=StringVar()

        self.price=DoubleVar()
        self.qty=IntVar()

        self.tlist=[]

        self.win.resizable(False, False)
        space=" "
        self.win.title(space*200+"Tela de pagamento")

        self.img = PhotoImage(file=r"Imagens/barra.png")
        heading=Label(self.win,text="Tela de pagamento", image=self.img)
        heading.pack()

        main_frame=Frame(self.win,background="yellow")
        main_frame.pack(fill="both",expand=1)

        customer_frame=LabelFrame(main_frame,pady=10,height=100,text="Informações do Cliente",font=("Elephant",15))
        customer_frame.place(x=0,y=30,width=1200)

        form_frame=LabelFrame(main_frame,height=400,pady=20,padx=20,width=410,text="Produtos",font=("Elephant",15))
        form_frame.place(x=0,y=130)

        table_frame=LabelFrame(main_frame,height=500,width=500, text="Detalhes da compra",font=("Elephant",15))
        table_frame.place(x=400,y=130)

        button_frame=LabelFrame(main_frame,height=135,width=400, text="Nota de pagamento", font=("Elephant",15))
        button_frame.place(x=0,y=530)

        botoesmenu_frame=LabelFrame(main_frame,height=30,width=900, borderwidth=0)
        botoesmenu_frame.place(x=0,y=0)

        #campo detalhes da compra
        Customer_Name_lbl=Label(customer_frame,text="Nome",font=("Arial",14))
        Customer_Name_lbl.place(x=5,y=0,width=80)
        Customer_Name_txt=Entry(customer_frame,font=("Arial",14),textvariable=self.cname)
        Customer_Name_txt.place(x=95,y=0)

        Customer_Mob_lbl=Label(customer_frame,text="CPF",font=("Arial",14))
        Customer_Mob_lbl.place(x=340,y=0,width=80)
        Customer_Mob_txt=Entry(customer_frame,font=("times new roman",15),textvariable=self.cmob)
        Customer_Mob_txt.place(x=430,y=0)

        #campo produtos
        Product_Cat=Label(form_frame,text="Categoria",font=("Arial",15))
        Product_Cat.place(x=0,y=0,width=130)
        self.categories.insert(0,"Selecione categoria")
        self.Product_Cat_List=ttk.Combobox(form_frame,font=("Arial",15),values=self.categories)
        self.Product_Cat_List.current(0)
        self.Product_Cat_List.place(x=160,y=0,width=200)

        self.Product_Cat_List.bind('<<ComboboxSelected>>',self.cat)

        Product_Sub=Label(form_frame,text="Sub Categoria",font=("Arial",14))
        Product_Sub.place(x=0,y=50,width=130)
        self.Product_Sub_List=ttk.Combobox(form_frame,font=("Arial",14))
        self.Product_Sub_List.place(x=160,y=50,width=200)

        Product_Rate_lbl=Label(form_frame,text="Preço",font=("Arial",14))
        Product_Rate_lbl.place(x=0,y=100,width=130)
        Product_Rate_txt=Entry(form_frame,font=("Arial",14),textvariable=self.price)
        Product_Rate_txt.place(x=160,y=100,width=200)

        Product_Qty_lbl=Label(form_frame,text="Qtd.",font=("Arial",14))
        Product_Qty_lbl.place(x=0,y=150,width=130)
        Product_Qty_txt=Entry(form_frame,font=("times new roman",15),textvariable=self.qty)
        Product_Qty_txt.place(x=160,y=150,width=200)

        #campo da nota de pagamento
        
        scrolly=Scrollbar(table_frame,orient=VERTICAL)
        self.billarea=Text(table_frame,yscrollcommand=scrolly.set,font=("arial",15),fg="black", height=21.5, width=52)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.billarea.yview)
        self.billarea.pack(fill=BOTH,expand=1)

        #Button
        self.Add_Item_Btn=Button(form_frame,text="Adicionar",font=("times new roman",15),command=self.addItem)
        self.Add_Item_Btn.place(x=30,y=200,width=100)

        self.Calc_Bill_Btn=Button(form_frame,text="Total",font=("times new roman",15),command=self.makeBill)
        self.Calc_Bill_Btn.place(x=150,y=200,width=70)

        self.Save_Bill_Btn=Button(button_frame,text="Salvar nota",font=("times new roman",15),command=self.save_bill)
        self.Save_Bill_Btn.place(x=30,y=25,width=100)

        self.Print_Btn=Button(button_frame,text="Imprimir",font=("times new roman",15),command=self.print_bill)
        self.Print_Btn.place(x=150,y=25,width=90)

        self.Reset_Btn=Button(form_frame,text="Limpar",font=("times new roman",15),command=self.reset)
        self.Reset_Btn.place(x=240,y=200,width=80)

        self.Exit_Btn=Button(button_frame,text="Cancelar",font=("times new roman",15),command=self.quit)
        self.Exit_Btn.place(x=260,y=25,width=90)

        self.voltar_Btn=Button(botoesmenu_frame,text="Voltar",font=("times new roman",10),command=self.voltar)
        self.voltar_Btn.place(x=0,y=5,width=80)

        self.heading()



    def cat(self,e=' '):
        if self.Product_Cat_List.get()=="Ingresso":
            self.Product_Sub_List.config(values=self.Ingresso)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Pipoca":
            self.Product_Sub_List.config(values=self.Pipoca)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Bebida":
            self.Product_Sub_List.config(values=self.Bebida)
            self.Product_Sub_List.current(0)

    def addItem(self):
        if self.Product_Cat_List.get()=="Selecione categoria":
            messagebox.showinfo("info","selecione uma categoria")
        elif self.price.get()==0:
            messagebox.showinfo("info","informe o preço do produto")
        elif self.qty.get()==0:
            messagebox.showinfo("info","informe a quantidade do produto")
        else:
            r=float(self.price.get())
            q=self.qty.get()
            t=r*q
            self.tlist.append(t)
            print(self.tlist)
            self.billarea.insert(END,f'\n       {q}\t       {self.Product_Sub_List.get()}       {r:05.2f}\t\t  {t:05.2f}')

    def makeBill(self):
        #if len(self.cname.get())==0 and len(self.cmob.get())==0 and len(self.cbill.get())==0:
        #    messagebox.showinfo("info","Informe os dados do cliente")
        if self.Product_Cat_List.get()=="Selecione categoria":
            messagebox.showinfo("info","Selecione uma categoria")
        elif self.price.get()==0:
            messagebox.showinfo("info","Informe o preço do produto")
        elif self.qty.get()==0:
            messagebox.showinfo("info","Informe a quantidade do produto")
        else:
            space=" "
            total=sum(self.tlist)
            self.billarea.insert(3.16,self.cname.get())
            self.billarea.insert(4.16 ,self.cmob.get())
            self.billarea.insert(END,"\\n-----------------------------------------------------------------------")
            self.billarea.insert(END,f'\n Total={space*63} {total}')

    def save_bill(self):
        opt=messagebox.askyesno("Bill","Deseja salvar conta?")
        if opt==True:
            self.bill_data=self.billarea.get(1.0,END)
            fh=open("bill/"+self.cbill.get()+".txt",'w')
            fh.write(self.bill_data)
            fh.close()
    def print_bill(self):
        q=self.billarea.get(1.0,'end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def reset(self):
        self.billarea.delete(1.0,END)
        self.heading()

    def quit(self):
        self.voltar()

    def heading(self):
        self.billarea.delete(1.0,END)
        self.billarea.insert(END,"\t\tCINEMALOCAL NOTA ")
        self.billarea.insert(END,"\n-----------------------------------------------------------------------")
        self.billarea.insert(END,f'\nNome:\t')
        self.billarea.insert(END,f'\nCPF :\t')
        self.billarea.insert(END,"\n-----------------------------------------------------------------------")
        self.billarea.insert(END,f'\nQuantidade\t             Produto\t                 Preço \t\t  Total')

    
    def voltar(self):
        self.win.destroy()
        janelas.Principal(self.carrinho)
    

if __name__=='__main__':
    win=Tk()
    app=Store(win)
    win.mainloop()