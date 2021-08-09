// 상품 데이터
const data = [
  { name: "초콜렛", price: 2000 },
  { name: "아이스크림", price: 1000 },
  { name: "컵라면", price: 1600 },
  { name: "볼펜", price: 2500 },
  { name: "아메리카노", price: 4000 },
  { name: "과자", price: 3000 },
  { name: "탄산수", price: 1200 },
  { name: "떡볶이", price: 3500 },
  { name: "노트", price: 1500 },
  { name: "껌", price: 500 },
];

// 사용자 입력 받기
const line = prompt("최대 금액을 입력해주세요.");
const amount = parseInt(line);

// 주어진 금액으로 살 수 있는 가장 비싼 상품을 구함
const item = getItemByAmount(data, amount);

const msg = item
  ? `${amount}원으로 살 수 있는 가장 비싼 상품은 [${item.name}]이고, 가격은 ${item.price}원입니다.`
  : "살 수 있는 상품이 없습니다.";

// 결과 출력
alert(msg);

// 아래에 getItemByAmount 함수를 작성하세요.
function getItemByAmount(data, amount) {
  let mostExpensiveItem = null; // 가장 비싼 아이템을 null로 설정합니다
  data
    .filter((item) => item.price <= amount)
    .map((item) => {
      if (mostExpensiveItem === null || item.price > mostExpensiveItem.price) {
        mostExpensiveItem = item; // 데이터를 돌며 아이템 가격이 amount 이하인 동시에 가장 비싼 아이템이 비어있거나 가격이 현재 아이템보다 적다면 현재 아이템을 가장 비싼 아이템으로 설정합니다.
      }
    });
  return mostExpensiveItem; // amount로 살 수 있는 가장 비싼 아이템 객체를 리턴합니다. 유효한 숫자가 아니면 자동적으로 null이 리턴됩니다.
}
