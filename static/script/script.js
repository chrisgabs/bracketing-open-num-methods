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
    // const eq = $("#eq").val()
    // const xu = $("#xu").val()
    // const xl = $("#xl").val()
    // const crit = $("#crit").val()
    data = JSON.stringify(data)
    console.log(data)
    $.post("receiver", data, function(response) {
        $("#output-container").append(response)
    })
}