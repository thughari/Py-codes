#'aa a234Bc@@# sAd$%% hsagD^',7


a='aa a234Bc@@# sAd$%% hsagD^'
c=0
for i in a:
    if(i==' ' or 48<=ord(i)<=57 or 65<=ord(i)<=90 or 97<=ord(i)<=122):
        pass
    else:
        c+=1
print(c)