course={'course':'AI/ML','instructor':'hussain','institute':'you excel'}
print(course)
print(type(course))

'''////////////////////////////////////////'''

course=['course','AI/ML','instructor','hussain','institute','you excel']
print(course)
print(type(course))

'''////////////////////////////////////////'''

course=dict(course='AI/ML',instructor='hussain',institute='you excel')
print(course)

'''////////////////////////////////////////'''

course={'course':'AI/ML','instructor':'hussain','institute':'you excel'}
print(course['instructor'])

'''////////////////////////////////////////'''

course={'course':'AI/ML','instructor':'hussain','institute':'you excel'}
print(course.keys()) #saari keys ko sirf print kary ga

'''////////////////////////////////////////'''

course={'course':'AI/ML','instructor':'hussain','institute':'you excel'}
print(course.values()) #saari key k undar ki values print kary ga

'''////////////////////////////////////////'''

course={'course':'AI/ML','instructor':'hussain','institute':'you excel'}
print(course.items()) #saary items bta dy ga

'''////////////////////////////////////////'''
course={'course':'AI/ML','instructor':'hussain','institute':'you excel'}
print(course.get('shah','not available'))  #if/else wala kaam krta hy ye, jo key hum comma se pehly likhy gy agar wo dict me hue
                                           #tw wo usko krdy ga wrna not available print kary ga

'''////////////////////////////////////////'''

course['email']='hussain8900.shs@gmail.com'
print(course)

'''///////////////////////////////////////'''

course['email']='03062148926.shs@gmail.com' #is email ne porani wali ko overright krdya
print(course)

'''///////////////////////////////////////'''

del course['course']  #dict me se course ko delete krdy ga ye
print(course)

'''////////////////////////////////////////'''

print(course.pop('institute')) #pop krdy ga institute ki value ko or print krdy ga

'''//////////////////////////////////////'''
course1={'course':'AI/ML','instructor':'hussain','institute':'you excel','timing':'600_930'}
print(course1)
for x in course1: #dic k undar jo keys hy usko print for ki help se
    print(x)
    
'''///////////////////////////////////////'''

print(course1)
for x in course1:   #dic k undar ko values hy usko print kary ga ye
    print(course1[x])
    
'''//////////////////////////////////////'''

print(course1)
for value in course1.values(): #values ko print kary ga
    print(value)
    
'''///////////////////////////////////////'''

uni= { 'std1':{'name':'syed baber','age':34},
       'std2':{'name':'hussain shah','age':38}, #ye nested dictionary hy
       'std3':{'name':'hammad hussain','age':67} 
    }
print(uni)
print(uni['std2'])

'''////////////////////////////////////////////'''

uni= { 'std1':{'name':'syed baber','age':34, 'class':{'section'}},
       'std2':{'name':'hussain shah','age':38}, #ye nested dictionary hy
       'std3':{'name':'hammad hussain','age':67} 
    }
print(uni)
print(uni['std1']['class'])

'''////////////////////////////////////////////'''

uni= { 'std1':{'name':'syed baber','age':34, 'class':{'section':'c'}},
       'std2':{'name':'hussain shah','age':38, 'class':{'section':'b'}}, #ye nested dictionary hy
       'std3':{'name':'hammad hussain','age':67,  'class':{'section':'a'}} 
    }
print(uni)
print(uni['std3']['class']['section'])