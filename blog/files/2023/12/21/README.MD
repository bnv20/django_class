CSS 선택자는 HTML 문서에서 특정 요소를 선택하여 스타일을 적용하는데 사용

1. 기본 선택자
전체 선택자 (*):
모든 요소에 스타일을 적용
예: * { margin: 0; padding: 0; }

태그 선택자 (Type Selector):
지정된 태그를 가진 모든 요소에 스타일을 적용
예: p { font-size: 16px; }

클래스 선택자 (.className):
지정된 클래스를 가진 모든 요소에 스타일을 적용
예: .menu { color: blue; }

ID 선택자 (#idName):
지정된 ID를 가진 단일 요소에 스타일을 적용
예: #header { background-color: gray; }

2. 복합 선택자
자손 선택자 (A B):
A 요소 내부의 모든 B 요소를 선택
예: div p { color: red; } (모든 div 내부의 p 요소에 적용)

자식 선택자 (A > B):
A 요소의 직접적인 자식인 B 요소를 선택
예: ul > li { list-style-type: square; } (모든 ul의 직접적인 자식 li에 적용)

인접 형제 선택자 (A + B):
A 요소 바로 다음에 오는 B 요소를 선택
예: h2 + p { margin-top: 0; } (h2 바로 다음에 오는 p에 적용)\

일반 형제 선택자 (A ~ B):
A 요소의 형제 중 모든 B 요소를 선택
예: h2 ~ p { line-height: 1.5; }

3. 속성 선택자
속성 존재 선택자 ([attribute]):
해당 속성을 가진 모든 요소를 선택
예: [disabled] { opacity: 0.5; }

속성 값 선택자 ([attribute="value"]):
지정된 속성 값을 가진 모든 요소를 선택
예: input[type="text"] { border-color: green; }

속성의 종류
- class : 요소를 스타일링하기 위해 css 클래스를 할당, 개발자가 임의로 지정
          의미 있는 이름, 재사용성, 일관성, 간결성, 충돌 방지를 고려
- id : 문서내에서 유일한 식별자를 제공. 
- href(Hypertext Reference) : 링크의 목적지 url
- src : <img>, <script>, <iframe> 등의 태그에서 사용되며 외부 리소승의 위치를 지정
- alt : <img> 태그에서 사용되며 이미지의 대체 텍스트를 제공
- type : <input>, <button>, <script> 등의 태그에서 사용되며 요소의 타입을 지정
- style : 인라인 CSS 스타일을 적용할 때 사용. 이 속성을 통해 요소에 직접적으로 스타일 지정

4. 의사 클래스 및 의사 요소
의사 클래스 (:pseudo-class):
특정 상태의 요소를 선택합니다. (예: :hover, :focus, :checked)
예: a:hover { color: red; }

의사 요소 (::pseudo-element):
요소의 특정 부분에 스타일을 적용(예: ::before, ::after, ::first-line)
예: p::first-letter { font-size: 2em; }

주요 CSS 속성
1. color
텍스트의 색상을 지정합니다.
예: color: red;, color: #FF0000;, color: rgb(255, 0, 0);
2. background
요소의 배경을 설정합니다. 색상, 이미지, 위치 등을 지정
예: background: blue;, background: url('image.jpg');, background: #FFFFFF url('image.jpg') no-repeat right top;
3. font-family
텍스트에 사용할 글꼴을 지정
예: font-family: 'Arial', sans-serif;
4. font-size
텍스트의 크기를 설정
예: font-size: 16px;, font-size: 1em;
5. border
요소의 테두리 스타일을 지정합니다. 너비, 스타일, 색상을 포함
예: border: 1px solid black;
6. margin
요소 외부의 여백을 지정. 상단, 우측, 하단, 좌측의 마진을 개별적으로 설정할 수 있다.
예: margin: 10px;, margin: 5px 10px 15px 20px;
7. padding
요소 내부의 여백을 지정. 내용과 테두리 사이의 공간을 조정.
예: padding: 10px;, padding: 5px 10px 15px 20px;
8. display
요소의 표시 유형을 결정. block, inline, inline-block, flex, grid, none 등이 있다.
예: display: block;, display: flex;
9. position
요소의 위치 지정 방식을 설정. static, relative, absolute, fixed, sticky 등이 있다.
예: position: relative;, position: absolute;
10. width 및 height
요소의 너비와 높이를 지정.
예: width: 100px;, height: 50%;
11. text-align
텍스트의 정렬 방식을 지정합니다. left, right, center, justify 등이 있다.
예: text-align: center;
12. opacity
요소의 투명도를 지정. 0에서 1 사이의 값을 가진다.
예: opacity: 0.5;
13. overflow
내용이 요소의 크기를 초과할 때의 처리 방법을 지정. visible, hidden, scroll, auto 등이 있다.
예: overflow: hidden;, overflow: scroll;
14. transition
속성 값의 변화에 대한 애니메이션 효과를 지정.
예: transition: all 0.3s ease;

