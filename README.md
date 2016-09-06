# redis-python-sample

## 5분동안의 방문자 저장 및 조회 알고리즘
### 우선 방문자 관련 API는 redis_test/views.py의 visit_count함수에 비즈니스 로직이 구현되어 있습니다.
> 우선 redis를 django의 cache로 사용하여 들어오는 방문자 수를 저장하였습니다.
> 캐시의 소멸은 5분마다 일어나게 하였습니다.

* POST
 > 먼저 POST방식으로 API가 들어오면, cache에서 해당 user_id가 있는지 없는지를 확인합니다.

 > 만약 cache에 해당 user_id의 방문수가 저장되어있지 않다면, user_id를 key로 1을 value로 cache에 저장합니다.

 > 기존에 cache에 user_id의 방문횟수가 저장되어 있다면, 해당 value를 받아와서 1을 증가시키고, cache에 수정된 값을 집어넣습니다.

* GET
 > GET방식으로 API가 들어오면, cache에서 user_id가 key인 value를 추출합니다.

 > 만약 value가 None이면 0을, None이 아니면 해당 value를 view단으로 렌더링합니다.

