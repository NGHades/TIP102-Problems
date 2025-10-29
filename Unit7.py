def count_layers(sandwich):
    """
    Understand
    Given one variable: nested list
    Returns int output
    
    Plan
    Base Case: len(list) == 0
    
    
    
    Implement
    """
    if len(sandwich) == 1:
        return 1
    return 1 + count_layers(sandwich[1])

# Example Usage
sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))

# Space: O(1)
# Time: O(n)


def reverse_orders(orders):
    """
    Understand
    Input: space-separated string orders
    Output: reversed string based on space separation
    
    Plan
    Use split method to turn string into lists, order_list = orders.split(" ")
    Base case: 
    order_str = ""
    reverse_orders(order_list[1::]) + "Bagel"
    
    
    Recursive call to build string as we go
    
    if len(list) == 1:
        we know its just one and we return string
    
    
    Implement
    """
    #[Bagel] + Coffee Sandwich 
    order_list = orders.split(" ")
    
    return reverse_orders_helper(order_list)
    
def reverse_orders_helper(order_list):
    if len(order_list) == 1:
        return order_list[0]
    return reverse_orders_helper(order_list[1::]) + " " + order_list[0]

print(reverse_orders("Bagel Sandwich Coffee"))
# Space: O(n) where n is the number of words
# Time: O(n^2), splicing a list costs O(n)
