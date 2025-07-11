# Git 브랜치 작업 플로우

## 브랜치 생성 방법

1. 원격 브랜치 목록 확인
   git branch -r

2. 원격 브랜치를 기반으로 새 브랜치 생성
   git branch [새 브랜치 이름] [원격 브랜치 이름]

예시:

```
git branch trie origin/ch15_trie
```

→ 원격 브랜치(대주제, 'origin/ch15_trie')를 기반으로, 새 로컬 브랜치(소주제, 'trie')를 만듭니다.
