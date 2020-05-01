print("##AARYAN KAPUR | E18CSE004 | LAB - DISK SCHEDULING ALGORITHMS ")


def FCFS(arr, head):
    seek_count = 0
    distance, cur_track = 0, 0
    for i in range(size):
        cur_track = arr[i]
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    print("Total number of seek operations = ", seek_count)
    print("Seek Sequence is")

    for i in range(size):
        print(arr[i])


#2 - SSTF
def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)


def findMin(diff):

    index = -1
    minimum = 999999999

    for i in range(len(diff)):
        if (not diff[i][1] and minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index


def SSTF(request, head):
    if (len(request) == 0):
        return

    l = len(request)
    diff = [0] * l
    for i in range(l):
        diff[i] = [0, 0]
    seek_count = 0
    seek_sequence = [0] * (l + 1)

    for i in range(l):
        seek_sequence[i] = head
        calculateDifference(request, head, diff)
        index = findMin(diff)

        diff[index][1] = True
        seek_count += diff[index][0]
        head = request[index]
    seek_sequence[len(seek_sequence) - 1] = head

    print("Total number of seek operations =", seek_count)

    print("Seek Sequence is")
    for i in range(l + 1):
        print(seek_sequence[i])

#3- SCAN
def SCAN(reqs, hp):
    requests = reqs.copy()
    pos = hp
    time = 0
    end = 200
    start = 0
    for i in range(pos, end + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            print( i)
            requests.remove(i)

    time += abs(pos - end)
    pos = end
    for i in range(end, start - 1, -1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            print( i)
            requests.remove(i)
    print(time)
    avg_seek_time = time 
    print("average seek time ", avg_seek_time)


def C_SCAN(reqs, hp):
    requests = reqs.copy()
    pos = hp
    time = 0
    end = 200
    start = 0
    for i in range(pos, end + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            print( i)
            requests.remove(i)
    time += abs(pos - end)
    pos = end
    for i in range(start, hp + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            print( i)
            requests.remove(i)

    avg_seek_time = time 
    print("average seek time ", avg_seek_time)


def LOOK(reqs, hp):
    requests = reqs.copy()
    pos = hp
    time = 0
    end = max(requests)
    start = min(requests)
    for i in range(pos, end + 1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            print( i)
            requests.remove(i)

    for i in range(end, start - 1, -1):
        if i in requests:
            time += abs(pos - i)
            pos = i
            print( i)
            requests.remove(i)
    print(time)
    avg_seek_time = time 
    print("average seek time ", avg_seek_time)


if __name__ == '__main__':
    arr = [45, 6, 8, 22, 176, 27, 77, 33, 30, 168, 190, 1, 3]
    head = 40
    size = len(arr)
    print("_________________________for FCFS_________________________")
    FCFS(arr, head)
    print("_________________________for SSTF_________________________")

    SSTF(arr, head)
    print("_________________________for SCAN_________________________")

    SCAN(arr, head)
    print("_________________________for C-SCAN_________________________")

    C_SCAN(arr, head)
    print("_________________________for LOOK_________________________")

    LOOK(arr, head)


print("##AARYAN KAPUR | E18CSE004 | LAB - DISK SCHEDULING ALGORITHMS ")
