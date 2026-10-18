# hong-iron.github.io

https://hong-iron.github.io/ 의 첫 화면입니다. 각 프로젝트는 자기 레포의 GitHub Pages(`/SMASH/`, `/SMASH-<학교>/`, `/Hongs_Blog/`)로 돌아가고, 이 레포는 주소 맨 위에만 필요한 파일을 둡니다.

- `site/index.html`: 첫 화면(SMASH 대학교, 블로그로 가는 링크)
- `site/robots.txt`: 검색 로봇은 주소 맨 위의 robots.txt만 읽습니다. 여기서 모든 사이트맵을 알려 줍니다.
- `site/sitemap.xml`: 첫 화면, SMASH 허브, SMASH 게임 전부. 학교를 추가하면 `python3 tools/build_sitemap.py <SMASH 레포>/schools.json`으로 다시 만듭니다. 블로그는 자체 사이트맵(`/Hongs_Blog/sitemap.xml`)을 씁니다.
- Google Search Console과 네이버 서치어드바이저의 소유 확인 파일도 `site/`에 둡니다(지우면 확인이 풀립니다).

`main`에 push하면 GitHub Actions가 `site/`를 GitHub Pages에 올립니다.
