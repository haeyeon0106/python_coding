from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque()     # 다리를 지나는 트럭을 담는 큐
    
    time = 0    # 현재시간
    current_weights = 0 # 다리 위를 지나는 트럭의 무게
    on_bridge_time = deque()    # 현재 다리 위에 있는 트럭들이 다리를 올라간 시간을 기록하는 큐
    
    while on_bridge or truck_weights:
        time += 1
        
        while on_bridge and time - on_bridge_time[0] >= bridge_length:
            current_weights -= on_bridge[0]
            on_bridge.popleft()
            on_bridge_time.popleft()
        
        # 지나가야 할 트럭이 존재하고 현재 다리 위에 있는 트럭의 무게 + 곧 지나갈 트럭의 무게가 weights보다 작을 경우(지나감)
        if truck_weights and current_weights + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            current_weights += truck
            on_bridge.append(truck)
            on_bridge_time.append(time)
            print(on_bridge_time)
    return time