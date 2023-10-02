from datetime import datetime

sample = [2, 3, 6, 8, 10, 49, 25]

x = 6

low = 0
high = len(sample) - 1

def binary_search(arr, x):
   low = 0
   high = len(arr) - 1
   mid = 0
 
   while low <= high:
      mid = (high + low) // 2

      if arr[mid] < x:
         low = mid + 1
      elif arr[mid] > x:
         high = mid - 1
      else:
         return mid
   return False

def binary_search2(x, sample, low, high):
   if low > high:
      return False
   else:
      mid = (low + high) // 2
      print(low, mid, high)
      if x == sample[mid]:
         return mid
      elif x > sample[mid]:
         return binary_search2(x, sample, mid + 1, high)
      elif x < sample[mid]:
         return binary_search2(x, sample, low, mid - 1)

print(binary_search(sample, x))
print(binary_search2(x, sample, low, high))