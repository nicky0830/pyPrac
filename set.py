#집합
#중복 원소 X, 순서 X

# set 생성 방법
fruits = {'apple', 'mango', 'orange'}
companies = set()

# set에 추가 방법
fruits.add('banana')
companies = {'apple','microsoft'}

# type : <class 'set'>
type(fruits) 
type(companies)

# 집합 연산 : 교집합, 합집합
fruits & companies
fruits | companies

# 리스트에 여러 세트를 담고 set 메서드 사용 
list_sets = [fruits, companies]
# 교집합
set.intersection(*list_sets)
# 합집합
set.union(*list_sets)
# 차집합
s1 = {1,2,3,4,5,6,7}
s2 = {3,6,9}
print(s1-s2) 
# {1,2,4,5,7}