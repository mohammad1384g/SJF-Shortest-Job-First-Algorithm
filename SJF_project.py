def data():
    try:
        number_of_processes=int(input("How many processes :"))
        if number_of_processes == 0:
            print("The number of processes more than zero")
            return None
    except ValueError:
        print("please enter the number:")
        return None
    
    processes=[]
    for i in range(number_of_processes):
      print(f"\n---process {i+1} ---")
      pid =i + 1
      arival_time=int(input(f"A.T  {pid}: "))
      execut_time=int(input(f"E.T  {pid} :"))
      processes.append({
            "pid": pid,
            "A.T": arival_time, 
            "E.T": execut_time,
            "W.T": 0,
            "finished" :False,
            "S.T" :0,
            "end_time" :0
        })
    return processes
    
def sjf_sort_do(processes):
    processes.sort(key=lambda p : p["E.T"])
    
    current_time = 0 #Time system 
    finished = 0
    n = len(processes)
    gant_chart = []
    print("\n+++++ SJF Processes")
    while  finished != n :
        ready_processes = []
        for p in processes:
         if not p["finished"] and p["A.T"] <= current_time:
           ready_processes.append(p)
        
        if len(ready_processes) == 0:
            current_time += 1
            continue
        shortest_job = min(ready_processes, key=lambda x: x["E.T"])
        # do it processes 
        shortest_job["S.T"] = current_time
        shortest_job["end_time"] = current_time + shortest_job["E.T"]
        shortest_job["W.T"] = shortest_job["S.T"] - shortest_job["A.T"]
        shortest_job["finished"] = True
        print(f"time {current_time} : p{shortest_job["pid"]} started")
        print(f"time {shortest_job['end_time']}: P{shortest_job['pid']} finished")
        gant_chart.append({
          "pid": shortest_job["pid"],
          "start": shortest_job["S.T"],
          "end": shortest_job["end_time"]
    })
    
        current_time = shortest_job["end_time"]
        finished+=1
        
    return gant_chart
def result(processes):
   print("++++++Final result+++++")
   print("PID\tA.T\tE.T\t S.T\tW.T")
   print("+-"*50)
   total_wating=0
   jam_zaman_kol = 0
   for p in processes:
      turnaround_time = p["end_time"] - p["A.T"]
      jam_zaman_kol+= turnaround_time
      print(f"{p["pid"]} \t {p["A.T"]} \t {p["E.T"]} \t {p["S.T"]} \t {p["W.T"]} ")
      total_wating+=p["W.T"] 

   avg_jam_zaman_kol = jam_zaman_kol / len(processes)
   print("-" * 60)
   print(f"The Avrage wating time is : {total_wating / len(processes)}")
   print(f"Average jam_zaman_kol Time: {avg_jam_zaman_kol:.2f}")
def gant_chart(gant_chart):
   print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Gant chart<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
   for g in gant_chart:
      print(f"|  P{g['pid']}  ", end="")
   print("|")
   for t in gant_chart:
        print(f"{t['start']:<7}", end="")
   print(f"{gant_chart[-1]['end']}")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<+SJF (Shortest Job First) Algorithm+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
processes = data()
if processes:
   gant=sjf_sort_do(processes)
   result(processes)
   gant_chart(gant)
else:
   print("No data entered!")
