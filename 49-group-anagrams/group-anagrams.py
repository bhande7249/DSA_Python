class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map={};
        for word in strs:
            key=str(sorted(word))
            if key not in hash_map:
                hash_map[key]=[];
            hash_map[key].append(word);
        return list(hash_map.values())