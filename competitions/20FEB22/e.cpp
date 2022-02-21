#include <iostream>
#include <queue>
using namespace std;

#define MAX_NUM 1001

int n, m;  //세로, 가로
int maps[MAX_NUM][MAX_NUM] = { 0, };  //전체 마을 지도 배열 선언
int hours[MAX_NUM][MAX_NUM] = { 0, };  //첫번째 바이러스 시간 경과 체크용 지도 배열 선언
int movement_x[5] = { 0, 0, 0 ,-1, 1 };
int movement_y[5] = { 0, -1, 1, 0, 0 };  //위, 아래, 왼쪽, 오른쪽에 대한 이동시 더해질 좌표값. 맨앞 0은 인덱스를 위한것으로 무시
int first_virus = 1;
int second_virus = 1;
int third_virus = 0;  //각 바이러스별 감염된 마을 수 초기화
queue<pair<int, int>> queue_virus;  //BFS에 사용할 큐 선언. 현재 지역
queue<pair<int, int>> queue_next_virus;  //감염될(진행중인) 지역에 대한 큐 선언

void BFS();  //BFS함수 선언

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;

	for (int i = 1; i <= n; ++i)
	{
		for (int j = 1; j <= m; ++j)
		{
			cin >> maps[i][j];

			if (maps[i][j] == 1 || maps[i][j] == 2)  //감염된 마을일 경우
			{
				queue_virus.push(make_pair(i, j));  //큐에 push
			}
		}
	}

	BFS();  //BFS 함수 호출

	cout << first_virus << " " << second_virus << " " << third_virus;

	return 0;
}


void BFS()
{
	int hour_count = 0;  //현재 시간

	do
	{
		int x = queue_virus.front().second;
		int y = queue_virus.front().first;  //front 값 복사
		queue_virus.pop();  //pop을 통한 큐 갱신

		if (maps[y][x] == 1)  //1번 바이러스에 대해서
		{
			for (int i = 1; i <= 4; ++i)
			{
				int next_y = y + movement_y[i];
				int next_x = x + movement_x[i];  //다음 좌표값 계산

				if (next_y > 0 && next_y <= n && next_x > 0 && next_x <= m)  //다음 좌표값이 지도 안에 존재한다면
				{
					if (maps[next_y][next_x] == 0)  //만약 다음 좌표의 마을이 감염되지 않았을 경우
					{
						maps[next_y][next_x] = 1;  //1번 바이러스 감염 처리
						first_virus++;  //바이러스 감염 수 갱신
						hours[next_y][next_x] = hour_count;  //시간 저장
						queue_next_virus.push(make_pair(next_y, next_x));  //다음에 퍼질 큐에 push
					}

					else if (maps[next_y][next_x] == 2 && hours[next_y][next_x] == hour_count)  
					//만약 다음 좌표의 마을이 이미 2번 바이러스에 감염되었고 1시간이 안지났을 경우
					{
						maps[next_y][next_x] = 3;  //3번 바이러스 감염처리
						third_virus++;
						second_virus--;  //각 바이러스별 감염 수 갱신
					}

				}
			}
		}

		else if (maps[y][x] == 2)  //2번 바이러스에 대해서
		{
			for (int i = 1; i <= 4; ++i)
			{
				int next_y = y + movement_y[i];
				int next_x = x + movement_x[i];  //다음 좌표값 계산

				if (next_y > 0 && next_y <= n && next_x > 0 && next_x <= m)  //다음 좌표값이 지도 안에 존재한다면
				{

					if (maps[next_y][next_x] == 0)  //만약 다음 좌표의 마을이 감염되지 않았을 경우
					{
						maps[next_y][next_x] = 2;  //2번 바이러스 감염 처리
						second_virus++;  //바이러스 감염 수 갱신
						hours[next_y][next_x] = hour_count;  //시간 저장
						queue_next_virus.push(make_pair(next_y, next_x));  //큐에 push
					}

					else if (maps[next_y][next_x] == 1 && hours[next_y][next_x] == hour_count)
					//만약 다음 좌표의 마을이 이미 1번 바이러스에 감염되었고 1시간이 안지났을 경우
					{
						maps[next_y][next_x] = 3;  //3번 바이러스 감염처리
						third_virus++;
						first_virus--;  //각 바이러스별 감염 수 갱신
					}
				}
			}
		}

		/*  마을 상태 확인용 출력 코드
		for (int i = 1; i <= n; ++i)
		{
			for (int j = 1; j <= m; ++j)
			{
				cout << maps[i][j] << " ";
			}

			cout << endl;
		}
		cout << endl;
		*/
		

		if (queue_virus.empty() == true && queue_next_virus.empty() == false)  //만약 현재 큐는 공백이고 진행중 큐는 공백이 아니라면
		{
			hour_count++;  //시간 증가
			queue_virus.swap(queue_next_virus);  //아직 바이러스가 퍼지고 있다는 뜻이므로 둘을 swap하여 전체 진행 상태를 갱신한다.
		}


	} while (queue_virus.empty() == false);  //현재 큐가 공백이 될 때까지
}