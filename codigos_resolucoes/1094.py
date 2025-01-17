import heapq


class Solution:
    """
    Este exercício cai na categoria de problemas resolvidos por Interval Partitioning
    """
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # Ordena as viagens pelo local de início
        trips_sorted = sorted(trips, key=lambda x: x[1])
        
        ongoing_rides = [] # Heap que adicionará as viagens no momento
        current_capacity = 0
        
        for trip in trips_sorted:
            num_passengers, start, end = trip
            
            # Remove todas as viagens que terminam antes ou no início da nova viagem
            while ongoing_rides and ongoing_rides[0][0] <= start:
                _, passengers_leaving = heapq.heappop(ongoing_rides)
                current_capacity -= passengers_leaving
            
            # Adiciona a nova viagem ao heap
            heapq.heappush(ongoing_rides, (end, num_passengers))
            current_capacity += num_passengers
            
            # Verifica se a capacidade foi excedida
            if current_capacity > capacity:
                return False
        
        return True
