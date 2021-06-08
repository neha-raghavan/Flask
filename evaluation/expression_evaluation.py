exp='( 5 + 10 ) / ( 8 * 6 )'
exp = '( -10 - 5 ) * 2 / 15 * 2 * ( 4 + 5 )'
# exp = '(5+10)' => ['(','5','+','10',')'] 
exp = "5+-10*(6+7)"
exp = "-1+1--1"
# (5+6+78)*2 like an expression has to be calculated
# tasks
# Split each numbers and operators as tokens
# Identify operators and numbers
# From the tokens generate a postfix epression
# evaluate the expression (postfix)

class Stack():
    top=-1
    arr=[]
    def push(self,data):
        self.arr.append(data)
        self.top=self.top+1
    def pop(self):
        self.top=self.top-1
        return self.arr.pop()
    def top_most(self):
        return self.arr[self.top]
    def is_empty(self):
        return (self.top == -1)
    

def Is_symbol(token):
    if (token=='+' or token=='-' or token=='*' or token=='/' or token=='(' or token==')'):
        return True
    else:
        return False
    

def preTokenise(incoming):
    result = []
    i = 0
    # (-401*6-(8+4))
    while i < len(incoming):
        if Is_symbol(incoming[i]):
            if incoming[i] == '-':
                if i != 0 and Is_symbol(incoming[i-1]):
                    i = i + 1
                    sample = []
                    sample.append('-')
                    while i<len(incoming) and Is_symbol(incoming[i]) is False:
                        sample.append(incoming[i])
                        i = i+1
                    result.append("".join(sample))
                elif (i==0):
                    sample=[]
                    sample.append('-')
                    i = i+1
                    while i<len(incoming) and Is_symbol(incoming[i]) is False:
                        sample.append(incoming[i])
                        i = i+1
                    result.append("".join(sample))
                else:
                    result.append(incoming[i])
                    i = i+1
            else:
                result.append(incoming[i])
                i = i + 1



        else:
            sample=[]
            while  i < len(incoming) and Is_symbol(incoming[i]) is False:
                sample.append(incoming[i])
                i=i+1
            result.append("".join(sample))
    return result




obj =Stack()
def check(token):
    if (token=='+' or token=='-' or token=='*' or token=='/'):
        return True
    else:
        return False
def precedence(token):
    if token=='+' or token== '-':
        return 1
    elif token=='*' or token=='/':
        return 2
    else:
        return 0


def infix_to_postfix(exp):
    output_list=[]
    tokens = preTokenise(exp)
    for token in tokens:
        if token =='(':
            obj.push(token)
        elif token == ')':
            while obj.is_empty() is False and obj.top_most()!='(':
                output_list.append(obj.pop())
            obj.pop()
        elif check(token) is False:
            output_list.append(token)
        else:
            while obj.is_empty() is False and precedence(token) >= precedence(obj.top_most()) and obj.top_most()!='(':
                output_list.append(obj.pop())
            obj.push(token)
    while obj.is_empty() is False:
        output_list.append(obj.pop())
    return output_list


def calculate(num1,num2,operator):
    if operator == '+':
        return num2+num1
    elif operator =='-':
        return num2-num1
    elif operator == '*':
        return num2 * num1
    else:
        return num2 / num1    

def evaluate(output_list):
    result=Stack()
    for item in  output_list:
        if check(item):
           num1=float(result.pop())
           num2=float(result.pop())
           result.push(calculate(num1,num2,item))
        else:
            result.push(item)
    return result.pop()


    
# hello my phone went off
# will join after switching on u stay
# i will come 
#ok
def infix_evaluation(expression):
    return evaluate(infix_to_postfix(expression))

