'''
당신은 쇼핑몰에서 상품을 검색할 수 있습니다. 검색어를 입력하면 검색어를 부분 문자열로 갖는 모든 상품들이 검색됩니다.
(부분 문자열이란? 문자열의 연속된 일부분을 의미합니다. 예를 들어 abcde의 부분 문자열은 abc나 bcde등이 있으며, ac, ea는 부분 문자열이 아닙니다.
특정 단어로 검색해서 검색된 상품의 개수가 하나일 때, 해당 단어를 상품의 고유 검색어라고 합니다.
당신은 상품마다 고유 검색어 중 가장 짧은 고유 검색어 목록을 구하려 합니다.

검색어 목록은 사전 순서대로 빠른 순으로 정렬되고, 중복되지 않아야 합니다.
검색어 목록은 공백 하나로 검색어들을 구분하는 형태입니다. 만약 고유 검색어가 없다면 None을 목록에 담습니다.

ex)
pencil : en nc pe
cilicon : ico ili lic
contrabase : a b
picturelist : u

쇼핑몰에 등록된 상품의 이름을 담은 문자열 배열 goods가 매개변수로 주어졌을 때, 가장 짧은 고유 검색어 목록을 순서대로
문자열 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
'''
def solution(goods):







solution(["pencil","cilicon","contrabase","picturelist"]) # 출력 결과는 ["en nc pe","ico ili lic","a b","u"]
solution(["abcdeabcd","cdabe","abce","bcdeab"]) # 출력 결과는 ["abcd eabc","be da","ce","None"]