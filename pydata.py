import os.path
with open('items.jl') as f:
    x = f.readlines() 
k="["    
for ch in x:
    if(ch=='\n'):
        k=k
    k+=ch
    k+=","
k= k[:-1]  
k+="]"
k.splitlines()   
save_path = r'C:\Users\TVS ROHITH\news extract\tutorial\Newswebsite'
with open(os.path.join(save_path,"objects.json"), "w") as text_file:
    print(f"{k}", file=text_file)
