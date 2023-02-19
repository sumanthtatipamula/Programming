#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/
#
# algorithms
# Medium (48.56%)
# Total Accepted:    62.9K
# Total Submissions: 129.5K
# Testcase Example:  '["bread"]\n[["yeast","flour"]]\n["yeast","flour","corn"]'
#
# You have information about n different recipes. You are given a string array
# recipes and a 2D string array ingredients. The i^th recipe has the name
# recipes[i], and you can create it if you have all the needed ingredients from
# ingredients[i]. Ingredients to a recipe may need to be created from other
# recipes, i.e., ingredients[i] may contain a string that is in recipes.
# 
# You are also given a string array supplies containing all the ingredients
# that you initially have, and you have an infinite supply of all of them.
# 
# Return a list of all the recipes that you can create. You may return the
# answer in any order.
# 
# Note that two recipes may contain each other in their ingredients.
# 
# 
# Example 1:
# 
# 
# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies =
# ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# 
# 
# Example 2:
# 
# 
# Input: recipes = ["bread","sandwich"], ingredients =
# [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create
# the ingredient "bread".
# 
# 
# Example 3:
# 
# 
# Input: recipes = ["bread","sandwich","burger"], ingredients =
# [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies =
# ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create
# the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the
# ingredients "bread" and "sandwich".
# 
# 
# 
# Constraints:
# 
# 
# n == recipes.length == ingredients.length
# 1 <= n <= 100
# 1 <= ingredients[i].length, supplies.length <= 100
# 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <=
# 10
# recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase
# English letters.
# All the values of recipes and supplies combined are unique.
# Each ingredients[i] does not contain any duplicate values.
# 
# 
#
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        suppliesset, plen, result, queue = set(supplies),  len(supplies) - 1, [], deque()
        [queue.append((r, i)) for r, i in zip(recipes, ingredients)]
        prev_len, curr_len = len(queue) - 1, len(queue)
        while(prev_len != curr_len):
            prev_len = curr_len
            for _ in range(len(queue)):
                recipe, ingredients = queue.popleft()
                if(all([ingredient in suppliesset for ingredient in ingredients])):
                    suppliesset.add(recipe)
                    result.append(recipe)
                else:
                    queue.append((recipe, ingredients))
            curr_len = len(queue)
        return result
        
