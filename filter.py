

# aggregated csv data
"""
id,imageUrl
6392963,https://st.kakaocdn.net/product/gift/product/y29ROOeKyyftcs8NxEgtAw/wGzci2FZl8ZMWKtPSOGjjWxEwlk6mQ6KoCbXE_5tICc
6392956,https://st.kakaocdn.net/product/gift/product/y29ROOeKyyftcs8NxEgtAw/bDd4jI4oErA1JCNXk63ga43nUkY4HlKYXZ4xs1NAQdY
6392951,https://st.kakaocdn.net/product/gift/product/y29ROOeKyyftcs8NxEgtAw/y5P2dneio0w-aoYMY3kI9-i7LSRVjLS8rIy6Lx2zNRw
3932856,https://st.kakaocdn.net/product/gift/product/y29ROOeKyyftcs8NxEgtAw/wnTTuHPYJSqvVFlAMjBOTm7KJyzM2_5xcGQ5PyOAl1s
"""

# result csv data

"""
image_url,version,score,tag
https://st.kakaocdn.net/product/gift/product/y29ROOeKyyftcs8NxEgtAw/wGzci2FZl8ZMWKtPSOGjjWxEwlk6mQ6KoCbXE_5tICc,vikingr_soft_adult_v24_05_25,2.126659559564814e-08,정상
https://st.kakaocdn.net/product/gift/product/y29ROOeKyyftcs8NxEgtAw/bDd4jI4oErA1JCNXk63ga43nUkY4HlKYXZ4xs1NAQdY,vikingr_soft_adult_v24_05_25,1.5389444385505158e-08,정상
https://st.kakaocdn.net/product/gift/product/y29ROOeKyyftcs8NxEgtAw/y5P2dneio0w-aoYMY3kI9-i7LSRVjLS8rIy6Lx2zNRw,vikingr_soft_adult_v24_05_25,9.827919711824507e-06,정상
"""

# read two csv files and filter out result csv data with id in aggregated csv data

import pandas as pd

import sys

category_id = sys.argv[1]

aggregated = pd.read_csv(f'{category_id}-aggregated.csv')

result = pd.read_csv(f'clean-result-{category_id}.csv')

result_filtered = result[result['image_url'].isin(aggregated['imageUrl'])]

# insert id column
result_filtered['id'] = result_filtered['image_url'].apply(lambda x: aggregated[aggregated['imageUrl'] == x]['id'].values[0])

print(len(result))
print(len(result_filtered))

result_filtered.to_csv(f'clean-result-filtered-{category_id}-with-id.csv', index=False)