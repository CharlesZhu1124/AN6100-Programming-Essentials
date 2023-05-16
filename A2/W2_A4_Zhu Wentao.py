# -*- coding: utf-8 -*-
"""
AN6100 PROGRAMMING ESSENTIALS 
2022
OOP Assignment

Due: Please refer to NTULearn
Worth: 5% to AN6100 final score.
Note: This assignment is an INDIVIDUAL assignment 

Submission instructions: You should submit only 1 W2_[Group][Index_Name].py  via the NTU-learn blackboard site. [Group] is either A or B.
Late penalty mark is computed based on 1% (out of the 5%)  every day after the submission due date. The submission score will be converted to 5%, then minus penalty marks, if appliable. The lower bound of the score is 0%. 
Please ensure that you include your name and index number in the .py file. You must keep a copy of the final version of your submission and be prepared to provide it on request. 
The University treats plagiarism, collusion, theft of other students’ work and other forms of dishonesty in assessment seriously. Students shared out their answers or copied answers from others shall receive a zero score.

Singapore retailers are either GST registered or non GST registered companies. 
Those companies which are non GST registered will print the price tag as simply as 

Price Tag
*********
papayas

Amount Payable : $   20.00 
===========================   

For companies that are GST registered, some choose to keep the customer informed of the original price before GST, some selected to state the price inclusive of GST.
The price tag for prices quoted inclusive of GST should look like :

Price Tag
*********
apples

Amount Payable : $   20.00
Including GST  : $    1.31 
===========================   

For those who did not include GST in the stated amount should have the price tag:

Price Tag
*********
oranges

Amount         : $   20.00
GST            : $    1.40
Amount Payable : $   21.40 
===========================  

You are given all classes and subclasses required to support the
printing of price tag.
You are given the full codes for PriceTag

You are requried replace all the 'pass' in the classes so that
you are able to test codes to run properly. 
 
"""

class GST:
    def __init__(self,initial_price,tax=0):
        self.initial_price=initial_price
        self.tax=tax
 
class inclusiveGST(GST):
    def __str__(self):
        add_tax=self.initial_price-self.initial_price/(1+self.tax/100)
        return f'''\nAmount Payable : ${self.initial_price:>8.2f}
Including GST  : ${add_tax:>8.2f}'''

class subjectToGST(GST):
    def __str__(self):
        sub_tax=self.initial_price*self.tax/100
        return f'''\nAmount         : ${self.initial_price:>8.2f}
GST            : ${sub_tax:>8.2f}
Amount Payable : ${self.initial_price+sub_tax:>8.2f}'''
        
class noGST(GST):
    def __str__(self):
        return f'\nAmount Payable : ${self.initial_price:>8.2f}'

class PriceTag():
    def __init__(self, item, gstObj):
        self.gstObj = gstObj
        self.item = item
    def __str__(self):
        return f'''
Price Tag
*********
{self.item}
{self.gstObj} 
===========================            
'''
        
if __name__ == "__main__":
    # kindly be reminded that there should be be any hardcoding 
    # of 7% in any of the classes above,
    #7 will be inserted as a parameter during instanitation of objects
    apple = inclusiveGST(20, 7)
    tag = PriceTag("apples", apple)
    print(tag)
    ''' expected output
Price Tag
*********
apples

Amount Payable : $   20.00
Including GST  : $    1.31
===========================
    '''

    orange = subjectToGST(20, 7)
    tag = PriceTag("oranges", orange)
    print(tag)
    ''' expected output
 Price Tag
 *********
 oranges

 Amount         : $   20.00
 GST            : $    1.40
 Amount Payable : $   21.40 
 ===========================   
    '''
    
    papaya = noGST(20)
    tag = PriceTag("papayas", papaya)
    print(tag)
    ''' expected output
Price Tag
*********
papayas

Amount Payable : $   20.00 
===========================     
    '''
    
    