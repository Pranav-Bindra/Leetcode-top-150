# First Approach :- o(N)
# Create 2 queues R and D and save the index at which they occur respectively. Initialize 2 pointers for each queue. If i<j, pop i and append it at the end of the queue, only remove j.
# Beats 34.01%



class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_queue = []
        D_queue = []

        for i in range(len(senate)):
            if senate[i] == 'R':
                R_queue.append(i)
            else:
                D_queue.append(i)

        i=0
        j=0
        while R_queue and D_queue:
            if R_queue[i]<D_queue[j]:
                x = R_queue.pop(i)
                R_queue.append(x+len(senate))
                D_queue.pop(i)
            else:
                x = D_queue.pop(i)
                D_queue.append(x+len(senate))
                R_queue.pop(i)

        if R_queue:
            return 'Radiant'
        else:
            return 'Dire'