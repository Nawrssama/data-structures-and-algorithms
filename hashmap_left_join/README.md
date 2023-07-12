# hashmap left join

> create a method that sorts a function based on the input array

# Approach & Efficiency

> Time ==> O(n)

> space ==> O(n)

# white-board

## hashmap left join
![hashmap left join ](.//hashmap%20left%20join.jpg)


# Solution 

    def left_join(synonyms, antonyms):
        joined_data = {}

        for key in synonyms:
            if key in antonyms:
                joined_data[key] = (synonyms[key], antonyms[key])
            else:
                joined_data[key] = (synonyms[key], None)

        return joined_data