---
title: "광고 수익 보고서 자동화"
date: "2023-03-03T16:59:46+09:00"
lastmod: "2023-05-19T17:44:39+09:00"
description: "여러 광고 매체의 수익 데이터를 수집하고 기간별 조회와 내려받기를 제공하는 사내 관리 도구를 개발했습니다."
summary: "여러 광고 매체의 수익 데이터를 수집하고 기간별 조회와 내려받기를 제공하는 사내 관리 도구를 개발했습니다."
tags: ["게임펍", "자동화", "백오피스"]
categories: ["프로젝트"]
hero: "images/adsreportdbupload.png"
menu:
  sidebar:
    name: "광고 수익 보고서 자동화"
    identifier: ad-report-admin
    parent: project
    weight: 30
---

## 개발 히스토리

사업부에서 매일 서비스 중인 게임들의 광고 수익을 지표로 만들고 있었는데 각 광고 수익 매체의 콘솔 사이트에 접속하여 원하는 데이터를 필터링 후 수기로 수집하고 있었다.
사업부는 이 작업으로 몇몇 인원들이 매일 2시간씩 소요되니 좀더 쉽게 자동화할 수 있는 방법이 없냐고 문의해왔다.

요구사항은 간단했다. 한 곳에서 모든 광고 매체의 광고수익 데이터들을 추출하게 해달라.

작업내역

* 각각의 광고매체 API 들을 이용하여 데이터베이스로 Insert.
* Admin 을 통해 원하는 데이터 검색기능 제공.
* 프로젝트, 기간별 필터링 기능과 CSV로 Export 제공.

## 설계

![광고 수익 보고서 자동화 참고 화면](images/adsreportdbupload.png)

## 프로젝트 관리

* 도커로 배포
* 젠킨스 빌드 배포 자동화

---

[기술 블로그에서 원문 보기](https://coolishbee.github.io/techblog/project/ad-report-admin/)
