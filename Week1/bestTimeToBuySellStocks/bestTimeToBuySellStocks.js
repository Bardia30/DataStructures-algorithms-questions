//sliding window algorithm
// Profit has to be more than zero
//want to return max profit. 
//initialize left pointer as buy = 0, init right pointer as sell = 1.

//if p[sell] - p[buy] < 0, we push buy to where we sold. 

//if p[sell] - p[buy] > maxProfit, we rplace it. 
//update sell 
//run while loop as long as sell is not at the end of the array 


const maxProfit = (prices) => {
    let buy = 0;
    let sell = 1;
    let maxProfit = 0;

    while (sell < prices.length) {
        let profit = prices[sell] - prices[buy]
        if (profit < 0) {
            buy = sell;
        }

        if (profit > maxProfit) {
            maxProfit = profit;
        }
        sell++;
    }

    return maxProfit;
}


console.log(maxProfit([2,1,2,1,0,1,2]))
