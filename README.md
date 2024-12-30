# FE_HeuristicAlgor
휴리스틱 알고리즘과 관련된 심화탐구

# Introducing

*<주의>*  pdf파일은 개인목적으로 재배포나 이용이 불가능합니다. 단순히 무슨 탐구를 했나 시사하는 용도입니다.


중학교 3학년때 구현을 포기한 '휴리스틱 알고리즘으로 최적의 길 찾기' 프로그램입니다.


당시엔 제 수준에 너무 어려워서 포기했었는데, 이제야 직접 만들어보네요.


여담으로 이 프로젝트들은 모두 제 고등학교 1학년 마지막 생기부중 개인심화탐구 분량으로 들어갑니다.


보고서에서는 제가 탐구를 하며 알게 된 휴리스틱 알고리즘들의 각각의 원리와 구체적인 구현 과정, 작동 과정, 결과 리뷰, 제언 등이 추가로 들어갈 것입니다.


소스코드에 따로 설명 주석이 달려있지는 않습니다.


직접 맵을 바꿔가며 시연해보고 싶으신 분들은 자유롭게 프로젝트를 다운받아서 그리드와 출발/도착지를 조정하시면서 작동시켜보시면 되겠습니다.


2024년의 마지막 작업물이자 고1의 끝을 장식하는 작업물이네요. 아주 감동적입니다.


2025년에는 더더욱 심화된 탐구들로 돌아오겠습니다.


감사합니다.

# Main Principle


f(n) : 총 예상 비용


g(n) : 출발지에서부터 n까지의 비용


h(n) : n으로부터 도착지까지의 비용



-----Dijkstra Algorithm-----


f(n) = g(n)


g값만 사용 / 8방향 이동 / 출발지에서부터 이동거리만 고려함



-----A* Algorithm-----


f(n) = g(n) + h(n) = g(n) + {(s.x - g.x)^2 + (s.y - g.y)^2}^(1/2) [Euclid]


g값과 휴리스틱 값 모두 사용 / 8방향 이동 / 출발지에서부터의 이동거리와 도착지까지의 필요한 이동거리를 모두 고려함


f(n) = g(n) + h(n) = g(n) + {abs(s.x - g.x) + abs(s.y - g.y)} [Manhatten]


g값과 휴리스틱 값 모두 사용 / 4방향 이동 / 출발지에서부터의 이동거리와 도착지까지의 필요한 이동거리를 모두 고려함



-----Greedy Algorithm-----


f(n) = h(n) = {(s.x - g.x)^2 + (s.y - g.y)^2}^(1/2)


휴리스틱 값만 사용 / 8방향 이동 / '탐욕' 말 그대로 현재 위치에서 최적의 선택지만 고려함



-----간단한 알고리즘 서술-----


OL : Open List


CL : Closed List


한 노드에서 인접한 j개의 노드까지의 총 예상비용을 f(n)으로 정함


인접한 j개의 노드를 허용범위내에서 OL로 append시킴


OL에 들어있는 노드중 f(n)이 가장 적은 노드를 pop함


허용범위를 만족할 경우 pop한 노드를 CL로 append 시킨 뒤 경로를 이어감


자세한 것은 참조된 png 파일 참조

# S-DUMBMAN

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=s-dumbman)](https://github.com/s-dumbman/github-readme-stats)


<a href="https://github.com/s-dumbman"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fseondal&count_bg=%23000000&title_bg=%23000000&icon=github.svg&icon_color=%23E7E7E7&title=GitHub&edge_flat=false)"/></a>
