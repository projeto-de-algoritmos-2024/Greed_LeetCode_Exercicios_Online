class Solution:
    """
    Esta solução usa o Inteval Scheduling, porém sem a ordenação. Logo, a complexidade cai para O(n)
    """

    def candy(self, ratings: list[int]) -> int:
        # Cada criança recebe um doce a princípio
        doces = [1] * len(ratings)
        
        # Faz duas varreduras no vetor para garantir a condição de que a criança com o maior rating receba mais doces que o vizinho com menos
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                doces[i] = doces[i-1] + 1
                
        for i in range(len(ratings)-2, -1, -1):
            print(i)
            if ratings[i] > ratings[i+1]:
                # Garantir que a criança i tenha mais doces que i+1
                doces[i] = max(doces[i], doces[i + 1] + 1)
            
        soma_doces = sum(doces)    
        
        return soma_doces