import Plyr from 'plyr'
import * as params from '@params'

const options = {
  ...params.videoplayer?.plyr,
  i18n: {
    restart: '처음부터 재생',
    rewind: '{seektime}초 뒤로',
    play: '재생',
    pause: '일시 정지',
    fastForward: '{seektime}초 앞으로',
    seek: '재생 위치',
    seekLabel: '전체 {duration} 중 {currentTime}',
    played: '재생한 시간',
    buffered: '불러온 시간',
    currentTime: '현재 시간',
    duration: '전체 시간',
    volume: '음량',
    mute: '음소거',
    unmute: '음소거 해제',
    enableCaptions: '자막 켜기',
    disableCaptions: '자막 끄기',
    download: '내려받기',
    enterFullscreen: '전체 화면',
    exitFullscreen: '전체 화면 종료',
    frameTitle: '{title} 재생기',
    captions: '자막',
    settings: '설정',
    pip: '작은 화면으로 보기',
    menuBack: '이전 메뉴로',
    speed: '재생 속도',
    normal: '기본',
    quality: '화질',
    loop: '반복',
    start: '시작',
    end: '종료',
    all: '전체',
    reset: '초기화',
    disabled: '사용 안 함',
    enabled: '사용',
    advertisement: '광고'
  }
}

window.addEventListener('DOMContentLoaded', () => Plyr.setup('.video-player', options))
