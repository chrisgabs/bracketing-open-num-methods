let selected = "Bisection"

$(function() {

    $("#calculate").on("click", () => onCalculate())
    
})

function onCalculate() {
    const bisection = ["eq", "xu", "xl", "crit"]
    let data = new Object()

    bisection.forEach(e => {
        const id = "#" + e
        data[e] = $(id).val()
    })
    data = JSON.stringify(data)

    $.post("receiver", data, function(response) {
        $("#output-container").append(response)
    })
}