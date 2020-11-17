/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault();
    const name = $('#name').val();
    const year = $('#year').val();
    const email = $('#email').val();
    const color = $('#color').val();
    const response = await axios.post('/api/get-lucky-num', {name,year,email,color});
    handleResponse(response);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(res) {
    const num = res.data.num;
    const year = res.data.year;
    //clear the DOM from errors after resubmission
    $('div b').empty();
    if(num && year){
        const numResult = `Your lucky number is ${num.num} (${num.fact}).`;
        const yearResult = `Your birth year (${year.year}) fact is ${year.fact}.`;
        $('#lucky-results').append(`<p>${numResult}</p>`).append(`<p>${yearResult}</p>`);
    } else {
        console.log(res.data);
        for (const property in res.data) {
            $(`#${property}-err`).text(res.data[property])
        }
    }
}

$("#lucky-form").on("submit",processForm);
