// 151. Reverse Words in a String
class Solution {
    public:
        string reverseWords(string s) {
            stringstream ss(s);
            string word, result = "";
            
            while (ss >> word) {
                    result = word + " " + result;         
            }
            if(result[0] == ' ')result.erase(0);
            if(result[result.size()-1] == ' ')result.erase(result.size()-1);
            
            return result;
        }
    };
    