for _ in range(int(input())):
        n , k = map(int,input().split())
        s = input()
        coun = 0
        for i in range(len(s)):
                
                if s[i] == '1' and k - 1 <= i:
                        if s[i - k + 1] == '0':
                                coun += 1
        print(coun)
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        