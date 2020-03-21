$(function(){
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "none",
        enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 50,
        titleTemplate : '<span class="title">#title#</span>',
        labels: {
            previous : 'Zurück',
            next : 'Weiter',
            finish : 'Bestätigen',
            current : ''
        }
    });
});
