const setLang = lang => {
    localStorage.setItem('lang', lang);
  }
  let lang = localStorage.getItem('lang');

  if(lang === null){
    lang = 'es'
    setLang(lang)
  }
  
  $.i18n().load({
    en,
    es
  })

  const updatePlaceholders = _ => {
    $( '#inputEmail' ).prop( {
        placeholder: $.i18n( 'inputEmail' ),
    } );

    $( '#inputPassword' ).prop( {
        placeholder: $.i18n( 'inputPassword' ),
    });
    $( '#inputFirstName' ).prop( {
        placeholder: $.i18n( 'inputFirstName' ),
    });
    $( '#inputLastName' ).prop( {
        placeholder: $.i18n( 'inputLastName' ),
    });
    $( '#repeatPassword' ).prop( {
      placeholder: $.i18n( 'repeatPassword' ),
  });
  }

  $('#lang-en').click( _ => {
    setLang('en')

    $.i18n({
      locale: 'en'
    });

    updatePlaceholders();
    $('body').i18n();
  })

  $('#lang-es').click( _ => {
    setLang('es')

    $.i18n({
      locale: 'es'
    });

    updatePlaceholders();
    $('body').i18n();
  })
  
  $.i18n({
    locale: lang
  });

  updatePlaceholders();
  $('body').i18n();