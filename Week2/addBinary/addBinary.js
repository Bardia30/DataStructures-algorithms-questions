const addBinary = (a, b) => {
    let result = "";
    let carry = 0;

    for (let i = 0; i < Math.max(a.length, b.length); i++) {
        const digitA  = i < a.length ? Number(a[a.length -1 - i]) : 0;
        const digitB = i < b.length ? Number(b[b.length - 1 - i]) : 0;
        
        const total = digitA + digitB + carry;

        const char = String(total % 2 );
        result = char + result;
        carry = Math.floor(total / 2);
    }

    if (carry!==0) {
        result = "1" + result;
    }
    return result;
}


console.log(addBinary("11", "1"))