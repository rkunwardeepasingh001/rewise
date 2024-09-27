# # def max_number(num_str):
# #     # Convert the string into a list of digits
# #     digits = list(num_str)
# #     # Sort the digits in descending order
# #     digits.sort(reverse=True)
# #     # Join the sorted digits back into a string
# #     max_num = ''.join(digits)
# #     print(max_num)
# #     return max_num

# # # Example usage
# # input_num = "101"
# # print(max_number(input_num))  # Output: 321

# def maximize_time(time: str) -> str:
#     # Replace '?' in hours
#     hours = list(time[:2])
#     minutes = list(time[3:])
    
#     # Maximize hours
#     if hours[0] == '?':
#         if hours[1] == '?' or hours[1] < '4':
#             hours[0] = '2'
#         else:
#             hours[0] = '1'
#     if hours[1] == '?':
#         if hours[0] == '2':
#             hours[1] = '3'
#         else:
#             hours[1] = '9'

#     # Maximize minutes
#     if minutes[0] == '?':
#         minutes[0] = '5'
#     if minutes[1] == '?':
#         minutes[1] = '9'

#     # Combine the hours and minutes back into the final time
#     latest_time = ''.join(hours) + ':' + ''.join(minutes)
#     return latest_time

# # Example usage
# input_time = "2?:3?"
# print(maximize_time(input_time))  # Output: 23:39

# def max_distance(benches: str) -> int:
#     # Convert the input string to a list for easier manipulation
#     benches_list = list(benches)
#     n = len(benches_list)
    
#     # List to store positions of people
#     people_positions = [i for i in range(n) if benches_list[i] == '1']
    
#     max_dist = 0
    
#     for i in range(n):
#         if benches_list[i] == '0':
#             # Calculate the distance to the closest person
#             dist_to_closest = min(abs(i - pos) for pos in people_positions)
#             max_dist = max(max_dist, dist_to_closest)
    
    
    
#         return max_dist

# # Example usage
# input_benches = "1000101"
# print(max_distance(input_benches))  # Output: 2


# def max_distance(benches):
#     import pdb;pdb.set_trace()
#     n = len(benches)
#     max_dist = 0
#     last_person_index = -1
  
#     for i in range(n):
#         if benches[i] == '1':
            
#             if last_person_index == -1:
            
#                 max_dist = i  
#             else:
                
#                 max_dist = max(max_dist, (i - last_person_index) // 2)
#             last_person_index = i

#     if last_person_index != -1:
#         max_dist = max(max_dist, n - last_person_index - 1)

#     return max_dist

# # Example usage
# input_benches = "1000"
# print(max_distance(input_benches))  # Output: 2
