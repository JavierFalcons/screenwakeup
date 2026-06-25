# -*- coding: utf-8 -*-
"""Translated content for ScreenWakeUp landing pages. Consumed by generate_landing_pages.py.

CONTENT[slug][lang] keys: title, desc, keywords, ogtitle, ogdesc, tag, h1, lead,
body (raw HTML, may contain {HOME}), cta, related [(label, sibling_slug)],
bc_self, howto {name,desc,steps:[(name,text)]} (optional), faq [(q,a)].
"""

CONTENT = {"prevent-teams-away": {}, "caffeine-alternative": {}, "keep-screen-awake-iphone": {}}

# ============================ prevent-teams-away ============================
CONTENT["prevent-teams-away"]["es"] = dict(
 title="Cómo evitar el estado Ausente en Teams (seguir en verde) — Gratis, sin instalar | ScreenWakeUp",
 desc="Evita que Microsoft Teams te marque como Ausente. Mantén tu estado en verde sin mover el ratón — herramienta web gratis, sin descargas ni permisos de administrador. Funciona en Windows, Mac y Chromebook.",
 keywords="evitar ausente teams, mantener teams activo, estado verde teams, teams ausente 5 minutos, seguir activo en teams, mover raton automatico",
 ogtitle="Cómo evitar el estado Ausente en Teams — seguir en verde sin mover el ratón",
 ogdesc="Herramienta web gratis que mantiene tu estado de Microsoft Teams como Activo. Sin descargas ni permisos de administrador.",
 tag="Microsoft Teams", h1='Cómo evitar el <span>estado Ausente en Teams</span>',
 lead="Mantén tu estado de Microsoft Teams en verde y Activo — sin mover el ratón, sin instalar nada y sin pedir permisos de administrador a TI.",
 body="""<p>Si Teams te pasa a <strong>Ausente</strong> en cuanto te alejas para leer, atender una llamada o concentrarte en otra ventana, no eres el único. Teams lee el <strong>temporizador de inactividad</strong> de tu sistema operativo: tras unos 5 minutos sin ratón ni teclado —o cuando la pantalla se bloquea o se suspende— cambia tu presencia a Ausente.</p>
  <div class="box"><strong>La solución en una línea:</strong> mantén reiniciado el temporizador de inactividad del sistema (y la pantalla despierta) desde una pestaña del navegador. Eso es justo lo que hace ScreenWakeUp: gratis, en tu navegador, sin instalar nada.</div>
  <h2>Mantén Teams Activo en 3 pasos</h2>
  <ol>
    <li><strong>Abre la herramienta.</strong> Ve a <a class="inline" href="{HOME}">screenwakeup.com</a> en Chrome o Edge, en una pestaña aparte.</li>
    <li><strong>Activa el anti-inactividad.</strong> Activa <strong>Simular movimiento del ratón</strong> y <strong>Enviar tecla F15 silenciosa</strong>.</li>
    <li><strong>Pulsa Mantener pantalla activa.</strong> Deja la pestaña abierta y visible. Tu estado seguirá en verde mientras la pestaña esté en marcha.</li>
  </ol>
  <h2>¿Por qué Teams me marca como Ausente?</h2>
  <p>Teams calcula tu presencia a partir del <strong>tiempo de inactividad del sistema</strong> y del <strong>estado de la pantalla</strong>. ScreenWakeUp resuelve ambas a la vez: mantiene un bloqueo de pantalla <em>y</em> envía una tecla <strong>F15</strong> silenciosa más un pequeño movimiento del puntero cada 55 segundos.</p>
  <h2>¿Por qué no una app de escritorio "mueve-ratón"?</h2>
  <ul>
    <li><strong>Sin instalación ni permisos de administrador</strong> — funciona en portátiles corporativos.</li>
    <li><strong>No guarda nada en tu equipo</strong> — se ejecuta en una pestaña.</li>
    <li><strong>Multiplataforma</strong> — Windows, macOS y Chromebook.</li>
    <li><strong>Gratis, sin cuenta</strong> — y además es temporizador Pomodoro y reloj a pantalla completa.</li>
  </ul>
  <h2>Preguntas frecuentes</h2>
  <h3>¿Va contra las normas de Microsoft Teams?</h3>
  <p>ScreenWakeUp nunca toca Teams, tu cuenta ni datos de la empresa: solo evita que la pantalla se suspenda y que salte el temporizador de inactividad. Sigue siempre las políticas de tu organización.</p>
  <h3>¿Funciona sin permisos de administrador?</h3>
  <p>Sí. Es solo una página web, no hay nada que instalar.</p>
  <h3>¿También funciona con Slack y Zoom?</h3>
  <p>Sí. El mismo método mantiene Slack como Activo y evita que Zoom te marque inactivo.</p>""",
 cta="Sigue en verde en Teams → abre la herramienta gratis",
 related=[("Alternativa gratis a Caffeine", "caffeine-alternative"), ("Mantener pantalla activa en iPhone", "keep-screen-awake-iphone")],
 bc_self="Evitar estado Ausente en Teams",
 howto=dict(name="Cómo evitar el estado Ausente en Microsoft Teams",
            desc="Mantén tu estado de Microsoft Teams en verde y Activo sin cambiar el ratón ni los ajustes del sistema.",
            steps=[("Abre la herramienta", "Abre screenwakeup.com en Chrome o Edge en una pestaña aparte."),
                   ("Activa el anti-inactividad", "Activa 'Simular movimiento del ratón' y 'Enviar tecla F15 silenciosa'."),
                   ("Activa", "Pulsa Mantener pantalla activa y deja la pestaña abierta.")]),
 faq=[("¿Por qué Teams me marca como Ausente?", "Microsoft Teams te marca como Ausente tras unos 5 minutos sin actividad de teclado o ratón, o cuando el equipo se bloquea o se suspende. Lee el temporizador de inactividad del sistema operativo."),
      ("¿Cómo mantengo el estado de Teams en verde sin mover el ratón?", "Abre screenwakeup.com, activa 'Simular movimiento del ratón' y 'Enviar tecla F15 silenciosa', y pulsa Mantener pantalla activa. Esto reinicia el temporizador de inactividad cada 55 segundos."),
      ("¿Va contra las normas de Microsoft Teams?", "ScreenWakeUp solo evita que la pantalla se suspenda y detiene el temporizador de inactividad. No accede a Teams, a tu cuenta ni a datos de la empresa. Sigue las políticas de tu organización."),
      ("¿Funciona sin permisos de administrador?", "Sí. Se ejecuta en la pestaña del navegador, sin instalación ni permisos de administrador.")],
)
CONTENT["prevent-teams-away"]["pt"] = dict(
 title="Como evitar o status Ausente no Teams (ficar verde) — Grátis, sem instalar | ScreenWakeUp",
 desc="Impeça que o Microsoft Teams mostre você como Ausente. Mantenha o status verde sem mexer o mouse — ferramenta web grátis, sem download nem direitos de administrador. Funciona no Windows, Mac e Chromebook.",
 keywords="evitar ausente teams, manter teams ativo, status verde teams, teams ausente 5 minutos, ficar ativo no teams, mexer mouse automatico",
 ogtitle="Como evitar o status Ausente no Teams — ficar verde sem mexer o mouse",
 ogdesc="Ferramenta web grátis que mantém seu status do Microsoft Teams como Ativo. Sem download nem direitos de administrador.",
 tag="Microsoft Teams", h1='Como evitar o <span>status Ausente no Teams</span>',
 lead="Mantenha seu status do Microsoft Teams verde e Ativo — sem mexer o mouse, sem instalar nada e sem pedir direitos de administrador.",
 body="""<p>Se o Teams te coloca como <strong>Ausente</strong> assim que você se afasta para ler, atender uma ligação ou focar em outra janela, você não está sozinho. O Teams lê o <strong>temporizador de inatividade</strong> do sistema operacional: após cerca de 5 minutos sem mouse ou teclado — ou quando a tela bloqueia ou suspende — ele muda sua presença para Ausente.</p>
  <div class="box"><strong>A solução em uma linha:</strong> mantenha o temporizador de inatividade reiniciado (e a tela acordada) a partir de uma aba do navegador. É exatamente o que o ScreenWakeUp faz: grátis, no navegador, sem instalar nada.</div>
  <h2>Mantenha o Teams Ativo em 3 passos</h2>
  <ol>
    <li><strong>Abra a ferramenta.</strong> Acesse <a class="inline" href="{HOME}">screenwakeup.com</a> no Chrome ou Edge, em uma aba separada.</li>
    <li><strong>Ative o anti-inatividade.</strong> Ative <strong>Simular movimento do mouse</strong> e <strong>Enviar tecla F15 silenciosa</strong>.</li>
    <li><strong>Clique em Manter tela ativa.</strong> Deixe a aba aberta e visível. Seu status fica verde enquanto a aba estiver rodando.</li>
  </ol>
  <h2>Por que o Teams me mostra como Ausente?</h2>
  <p>O Teams calcula sua presença a partir do <strong>tempo de inatividade do sistema</strong> e do <strong>estado da tela</strong>. O ScreenWakeUp resolve os dois ao mesmo tempo: mantém um bloqueio de tela <em>e</em> envia uma tecla <strong>F15</strong> silenciosa mais um pequeno movimento do ponteiro a cada 55 segundos.</p>
  <h2>Por que não um app de desktop "mexe-mouse"?</h2>
  <ul>
    <li><strong>Sem instalação nem direitos de administrador</strong> — funciona em notebooks corporativos.</li>
    <li><strong>Não guarda nada na sua máquina</strong> — roda em uma aba.</li>
    <li><strong>Multiplataforma</strong> — Windows, macOS e Chromebook.</li>
    <li><strong>Grátis, sem conta</strong> — e ainda é timer Pomodoro e relógio em tela cheia.</li>
  </ul>
  <h2>Perguntas frequentes</h2>
  <h3>Vai contra as regras do Microsoft Teams?</h3>
  <p>O ScreenWakeUp nunca toca no Teams, na sua conta nem em dados da empresa: só impede a tela de suspender e o temporizador de inatividade de disparar. Siga sempre as políticas da sua organização.</p>
  <h3>Funciona sem direitos de administrador?</h3>
  <p>Sim. É apenas uma página web, não há nada para instalar.</p>
  <h3>Também funciona com Slack e Zoom?</h3>
  <p>Sim. O mesmo método mantém o Slack Ativo e impede o Zoom de te marcar como inativo.</p>""",
 cta="Fique verde no Teams → abra a ferramenta grátis",
 related=[("Alternativa grátis ao Caffeine", "caffeine-alternative"), ("Manter tela ativa no iPhone", "keep-screen-awake-iphone")],
 bc_self="Evitar status Ausente no Teams",
 howto=dict(name="Como evitar o status Ausente no Microsoft Teams",
            desc="Mantenha seu status do Microsoft Teams verde e Ativo sem mudar o mouse nem as configurações do sistema.",
            steps=[("Abra a ferramenta", "Abra screenwakeup.com no Chrome ou Edge em uma aba separada."),
                   ("Ative o anti-inatividade", "Ative 'Simular movimento do mouse' e 'Enviar tecla F15 silenciosa'."),
                   ("Ative", "Clique em Manter tela ativa e deixe a aba aberta.")]),
 faq=[("Por que o Teams me mostra como Ausente?", "O Microsoft Teams te marca como Ausente após cerca de 5 minutos sem atividade de teclado ou mouse, ou quando o computador bloqueia ou suspende. Ele lê o temporizador de inatividade do sistema."),
      ("Como mantenho o status do Teams verde sem mexer o mouse?", "Abra screenwakeup.com, ative 'Simular movimento do mouse' e 'Enviar tecla F15 silenciosa', e clique em Manter tela ativa. Isso reinicia o temporizador a cada 55 segundos."),
      ("Vai contra as regras do Microsoft Teams?", "O ScreenWakeUp só impede a tela de suspender e para o temporizador de inatividade. Não acessa o Teams, sua conta nem dados da empresa. Siga as políticas da sua organização."),
      ("Funciona sem direitos de administrador?", "Sim. Roda na aba do navegador, sem instalação nem permissões de administrador.")],
)
CONTENT["prevent-teams-away"]["fr"] = dict(
 title="Comment éviter le statut Absent sur Teams (rester vert) — Gratuit, sans installation | ScreenWakeUp",
 desc="Empêchez Microsoft Teams de vous afficher comme Absent. Gardez votre statut vert sans bouger la souris — outil web gratuit, sans téléchargement ni droits administrateur. Fonctionne sur Windows, Mac et Chromebook.",
 keywords="éviter absent teams, garder teams actif, statut vert teams, teams absent 5 minutes, rester actif teams, bouger souris automatique",
 ogtitle="Comment éviter le statut Absent sur Teams — rester vert sans bouger la souris",
 ogdesc="Outil web gratuit qui garde votre statut Microsoft Teams Actif. Sans téléchargement ni droits administrateur.",
 tag="Microsoft Teams", h1='Comment éviter le <span>statut Absent sur Teams</span>',
 lead="Gardez votre statut Microsoft Teams vert et Actif — sans bouger la souris, sans rien installer et sans demander de droits administrateur.",
 body="""<p>Si Teams vous bascule en <strong>Absent</strong> dès que vous vous éloignez pour lire, prendre un appel ou vous concentrer sur une autre fenêtre, vous n'êtes pas seul. Teams lit le <strong>minuteur d'inactivité</strong> de votre système : après environ 5 minutes sans souris ni clavier — ou quand l'écran se verrouille ou se met en veille — il passe votre présence à Absent.</p>
  <div class="box"><strong>La solution en une ligne :</strong> gardez le minuteur d'inactivité réinitialisé (et l'écran éveillé) depuis un onglet du navigateur. C'est exactement ce que fait ScreenWakeUp : gratuit, dans votre navigateur, sans installation.</div>
  <h2>Gardez Teams Actif en 3 étapes</h2>
  <ol>
    <li><strong>Ouvrez l'outil.</strong> Allez sur <a class="inline" href="{HOME}">screenwakeup.com</a> dans Chrome ou Edge, dans un onglet séparé.</li>
    <li><strong>Activez l'anti-inactivité.</strong> Activez <strong>Simuler le mouvement de la souris</strong> et <strong>Envoyer la touche F15 silencieuse</strong>.</li>
    <li><strong>Cliquez sur Garder l'écran éveillé.</strong> Laissez l'onglet ouvert et visible. Votre statut reste vert tant que l'onglet tourne.</li>
  </ol>
  <h2>Pourquoi Teams m'affiche-t-il comme Absent ?</h2>
  <p>Teams calcule votre présence à partir du <strong>temps d'inactivité du système</strong> et de l'<strong>état de l'écran</strong>. ScreenWakeUp gère les deux à la fois : il maintient un verrou d'écran <em>et</em> envoie une touche <strong>F15</strong> silencieuse plus un petit mouvement du pointeur toutes les 55 secondes.</p>
  <h2>Pourquoi pas une appli de bureau « anti-veille » ?</h2>
  <ul>
    <li><strong>Sans installation ni droits administrateur</strong> — fonctionne sur les ordinateurs d'entreprise verrouillés.</li>
    <li><strong>Ne stocke rien sur votre machine</strong> — tourne dans un onglet.</li>
    <li><strong>Multiplateforme</strong> — Windows, macOS et Chromebook.</li>
    <li><strong>Gratuit, sans compte</strong> — et fait aussi minuteur Pomodoro et horloge plein écran.</li>
  </ul>
  <h2>Questions fréquentes</h2>
  <h3>Est-ce contraire aux règles de Microsoft Teams ?</h3>
  <p>ScreenWakeUp ne touche jamais à Teams, à votre compte ni aux données de l'entreprise : il empêche seulement la mise en veille de l'écran et le déclenchement du minuteur d'inactivité. Suivez toujours les règles de votre organisation.</p>
  <h3>Fonctionne-t-il sans droits administrateur ?</h3>
  <p>Oui. C'est juste une page web, rien à installer.</p>
  <h3>Fonctionne-t-il aussi avec Slack et Zoom ?</h3>
  <p>Oui. La même méthode garde Slack Actif et empêche Zoom de vous marquer inactif.</p>""",
 cta="Restez vert sur Teams → ouvrez l'outil gratuit",
 related=[("Alternative gratuite à Caffeine", "caffeine-alternative"), ("Garder l'écran de l'iPhone allumé", "keep-screen-awake-iphone")],
 bc_self="Éviter le statut Absent sur Teams",
 howto=dict(name="Comment éviter le statut Absent sur Microsoft Teams",
            desc="Gardez votre statut Microsoft Teams vert et Actif sans changer la souris ni les réglages système.",
            steps=[("Ouvrez l'outil", "Ouvrez screenwakeup.com dans Chrome ou Edge dans un onglet séparé."),
                   ("Activez l'anti-inactivité", "Activez 'Simuler le mouvement de la souris' et 'Envoyer la touche F15 silencieuse'."),
                   ("Activez", "Cliquez sur Garder l'écran éveillé et laissez l'onglet ouvert.")]),
 faq=[("Pourquoi Teams m'affiche-t-il comme Absent ?", "Microsoft Teams vous marque Absent après environ 5 minutes sans activité clavier ou souris, ou quand l'ordinateur se verrouille ou se met en veille. Il lit le minuteur d'inactivité du système."),
      ("Comment garder mon statut Teams vert sans bouger la souris ?", "Ouvrez screenwakeup.com, activez 'Simuler le mouvement de la souris' et 'Envoyer la touche F15 silencieuse', puis cliquez sur Garder l'écran éveillé. Cela réinitialise le minuteur toutes les 55 secondes."),
      ("Est-ce contraire aux règles de Microsoft Teams ?", "ScreenWakeUp empêche seulement la mise en veille de l'écran et arrête le minuteur d'inactivité. Il n'accède pas à Teams, à votre compte ni aux données de l'entreprise. Suivez les règles de votre organisation."),
      ("Fonctionne-t-il sans droits administrateur ?", "Oui. Il tourne dans l'onglet du navigateur, sans installation ni permissions administrateur.")],
)
CONTENT["prevent-teams-away"]["de"] = dict(
 title="Teams-Status Abwesend verhindern (grün bleiben) — Kostenlos, ohne Installation | ScreenWakeUp",
 desc="Verhindern Sie, dass Microsoft Teams Sie als Abwesend anzeigt. Halten Sie Ihren Status grün, ohne die Maus zu bewegen — kostenloses Web-Tool, ohne Download oder Administratorrechte. Funktioniert unter Windows, Mac und Chromebook.",
 keywords="teams abwesend verhindern, teams aktiv halten, teams grüner status, teams abwesend nach 5 minuten, in teams aktiv bleiben, maus bewegen automatisch",
 ogtitle="Teams-Status Abwesend verhindern — grün bleiben ohne die Maus zu bewegen",
 ogdesc="Kostenloses Web-Tool, das Ihren Microsoft-Teams-Status Aktiv hält. Ohne Download oder Administratorrechte.",
 tag="Microsoft Teams", h1='Den <span>Teams-Status Abwesend</span> verhindern',
 lead="Halten Sie Ihren Microsoft-Teams-Status grün und Aktiv — ohne die Maus zu bewegen, ohne etwas zu installieren und ohne Administratorrechte.",
 body="""<p>Wenn Teams Sie auf <strong>Abwesend</strong> schaltet, sobald Sie zum Lesen aufstehen, telefonieren oder sich auf ein anderes Fenster konzentrieren, sind Sie nicht allein. Teams liest den <strong>Inaktivitäts-Timer</strong> Ihres Betriebssystems: nach etwa 5 Minuten ohne Maus oder Tastatur — oder wenn der Bildschirm sperrt oder schläft — wechselt es Ihre Präsenz auf Abwesend.</p>
  <div class="box"><strong>Die Lösung in einem Satz:</strong> Halten Sie den Inaktivitäts-Timer (und den Bildschirm wach) über einen Browser-Tab zurückgesetzt. Genau das macht ScreenWakeUp: kostenlos, im Browser, ohne Installation.</div>
  <h2>Teams in 3 Schritten Aktiv halten</h2>
  <ol>
    <li><strong>Tool öffnen.</strong> Gehen Sie zu <a class="inline" href="{HOME}">screenwakeup.com</a> in Chrome oder Edge, in einem separaten Tab.</li>
    <li><strong>Anti-Inaktivität aktivieren.</strong> Aktivieren Sie <strong>Mausbewegung simulieren</strong> und <strong>Stille F15-Taste senden</strong>.</li>
    <li><strong>Bildschirm wach halten klicken.</strong> Lassen Sie den Tab offen und sichtbar. Ihr Status bleibt grün, solange der Tab läuft.</li>
  </ol>
  <h2>Warum zeigt Teams mich als Abwesend?</h2>
  <p>Teams berechnet Ihre Präsenz aus der <strong>System-Inaktivitätszeit</strong> und dem <strong>Bildschirmzustand</strong>. ScreenWakeUp löst beides zugleich: Es hält eine Bildschirmsperre <em>und</em> sendet alle 55 Sekunden eine stille <strong>F15</strong>-Taste plus eine winzige Zeigerbewegung.</p>
  <h2>Warum keine Desktop-"Maus-Wackler"-App?</h2>
  <ul>
    <li><strong>Ohne Installation oder Administratorrechte</strong> — funktioniert auf gesperrten Firmen-Laptops.</li>
    <li><strong>Speichert nichts auf Ihrem Rechner</strong> — läuft in einem Tab.</li>
    <li><strong>Plattformübergreifend</strong> — Windows, macOS und Chromebook.</li>
    <li><strong>Kostenlos, ohne Konto</strong> — und zugleich Pomodoro-Timer und Vollbild-Uhr.</li>
  </ul>
  <h2>Häufige Fragen</h2>
  <h3>Verstößt das gegen die Regeln von Microsoft Teams?</h3>
  <p>ScreenWakeUp berührt niemals Teams, Ihr Konto oder Firmendaten: Es verhindert nur, dass der Bildschirm schläft und der Inaktivitäts-Timer auslöst. Befolgen Sie stets die Richtlinien Ihrer Organisation.</p>
  <h3>Funktioniert es ohne Administratorrechte?</h3>
  <p>Ja. Es ist nur eine Webseite, nichts zu installieren.</p>
  <h3>Funktioniert es auch mit Slack und Zoom?</h3>
  <p>Ja. Dieselbe Methode hält Slack Aktiv und verhindert, dass Zoom Sie als inaktiv markiert.</p>""",
 cta="In Teams grün bleiben → kostenloses Tool öffnen",
 related=[("Kostenlose Caffeine-Alternative", "caffeine-alternative"), ("iPhone-Bildschirm wach halten", "keep-screen-awake-iphone")],
 bc_self="Teams-Status Abwesend verhindern",
 howto=dict(name="So verhindern Sie den Abwesend-Status in Microsoft Teams",
            desc="Halten Sie Ihren Microsoft-Teams-Status grün und Aktiv, ohne Maus oder Systemeinstellungen zu ändern.",
            steps=[("Tool öffnen", "Öffnen Sie screenwakeup.com in Chrome oder Edge in einem separaten Tab."),
                   ("Anti-Inaktivität aktivieren", "Aktivieren Sie 'Mausbewegung simulieren' und 'Stille F15-Taste senden'."),
                   ("Aktivieren", "Klicken Sie auf Bildschirm wach halten und lassen Sie den Tab offen.")]),
 faq=[("Warum zeigt Teams mich als Abwesend?", "Microsoft Teams markiert Sie nach etwa 5 Minuten ohne Tastatur- oder Mausaktivität als Abwesend, oder wenn der Computer sperrt oder schläft. Es liest den Inaktivitäts-Timer des Systems."),
      ("Wie halte ich meinen Teams-Status grün, ohne die Maus zu bewegen?", "Öffnen Sie screenwakeup.com, aktivieren Sie 'Mausbewegung simulieren' und 'Stille F15-Taste senden' und klicken Sie auf Bildschirm wach halten. Das setzt den Timer alle 55 Sekunden zurück."),
      ("Verstößt das gegen die Regeln von Microsoft Teams?", "ScreenWakeUp verhindert nur, dass der Bildschirm schläft, und stoppt den Inaktivitäts-Timer. Es greift nicht auf Teams, Ihr Konto oder Firmendaten zu. Befolgen Sie die Richtlinien Ihrer Organisation."),
      ("Funktioniert es ohne Administratorrechte?", "Ja. Es läuft im Browser-Tab, ohne Installation oder Administratorrechte.")],
)
CONTENT["prevent-teams-away"]["ja"] = dict(
 title="Teams の「退席中」を防ぐ方法（オンライン表示を維持）— 無料・インストール不要 | ScreenWakeUp",
 desc="Microsoft Teams に「退席中」と表示されないようにします。マウスを動かさずにステータスを緑のまま維持 — 無料のウェブツール、ダウンロードや管理者権限は不要。Windows・Mac・Chromebook で動作。",
 keywords="teams 退席中 防ぐ, teams アクティブ 維持, teams 緑 ステータス, teams 5分 退席中, teams アクティブのまま, マウス 自動 動かす",
 ogtitle="Teams の「退席中」を防ぐ方法 — マウスを動かさずに緑を維持",
 ogdesc="Microsoft Teams のステータスをアクティブに保つ無料ウェブツール。ダウンロードや管理者権限は不要。",
 tag="Microsoft Teams", h1='Teams の<span>「退席中」を防ぐ</span>方法',
 lead="マウスを動かさず、何もインストールせず、管理者権限も求めずに — Microsoft Teams のステータスを緑（アクティブ）のまま維持します。",
 body="""<p>読み物や電話、別ウィンドウへの集中などで少し離れた途端に Teams が<strong>「退席中」</strong>に切り替わる——よくあることです。Teams は OS の<strong>アイドルタイマー</strong>を読み取り、マウスやキーボードの操作が約5分ない場合、または画面がロック・スリープした場合に、プレゼンスを「退席中」に変更します。</p>
  <div class="box"><strong>解決策はひとつ:</strong> ブラウザのタブからシステムのアイドルタイマーをリセットし続け（かつ画面を起こしたまま）にします。それがまさに ScreenWakeUp の機能です。無料・ブラウザ内・インストール不要。</div>
  <h2>3ステップで Teams をアクティブに保つ</h2>
  <ol>
    <li><strong>ツールを開く。</strong> Chrome または Edge で別タブに <a class="inline" href="{HOME}">screenwakeup.com</a> を開きます。</li>
    <li><strong>アイドル防止を有効化。</strong> <strong>マウス移動をシミュレート</strong>と<strong>無音の F15 キーを送信</strong>をオンにします。</li>
    <li><strong>「画面をスリープさせない」をクリック。</strong> タブを開いたまま表示しておきます。タブが動いている間、ステータスは緑のままです。</li>
  </ol>
  <h2>なぜ Teams は「退席中」と表示するのか</h2>
  <p>Teams はプレゼンスを<strong>システムのアイドル時間</strong>と<strong>画面の状態</strong>から判定します。ScreenWakeUp は両方に同時に対応します。画面のウェイクロックを保持し、<em>かつ</em>55秒ごとに無音の <strong>F15</strong> キーと小さなポインタ移動を送信します。</p>
  <h2>デスクトップの「マウス揺らし」アプリではダメ？</h2>
  <ul>
    <li><strong>インストール・管理者権限が不要</strong> — ソフトを入れられない社用 PC でも動作。</li>
    <li><strong>端末に何も保存しない</strong> — タブ内で動作。</li>
    <li><strong>クロスプラットフォーム</strong> — Windows・macOS・Chromebook。</li>
    <li><strong>無料・アカウント不要</strong> — ポモドーロタイマーや全画面時計にもなります。</li>
  </ul>
  <h2>よくある質問</h2>
  <h3>Microsoft Teams の規約に違反しますか？</h3>
  <p>ScreenWakeUp は Teams・アカウント・社内データには一切触れません。画面のスリープとアイドルタイマーの作動を防ぐだけです。必ず所属組織のポリシーに従ってください。</p>
  <h3>管理者権限なしで動きますか？</h3>
  <p>はい。ただのウェブページなので、インストールするものはありません。</p>
  <h3>Slack や Zoom でも使えますか？</h3>
  <p>はい。同じ方法で Slack をアクティブに保ち、Zoom にアイドルと判定されるのを防ぎます。</p>""",
 cta="Teams で緑を維持 → 無料ツールを開く",
 related=[("無料の Caffeine 代替", "caffeine-alternative"), ("iPhone の画面をスリープさせない", "keep-screen-awake-iphone")],
 bc_self="Teams の退席中を防ぐ",
 howto=dict(name="Microsoft Teams の「退席中」を防ぐ方法",
            desc="マウスやシステム設定を変えずに、Microsoft Teams のステータスを緑（アクティブ）のまま維持します。",
            steps=[("ツールを開く", "Chrome または Edge で別タブに screenwakeup.com を開きます。"),
                   ("アイドル防止を有効化", "「マウス移動をシミュレート」と「無音の F15 キーを送信」をオンにします。"),
                   ("有効化", "「画面をスリープさせない」をクリックし、タブを開いたままにします。")]),
 faq=[("なぜ Teams は私を「退席中」と表示するのですか？", "Microsoft Teams は、キーボードやマウスの操作が約5分間ない場合、またはコンピュータがロック・スリープした場合に「退席中」と表示します。OS のアイドルタイマーを読み取っています。"),
      ("マウスを動かさずに Teams のステータスを緑に保つには？", "screenwakeup.com を開き、「マウス移動をシミュレート」と「無音の F15 キーを送信」をオンにして、「画面をスリープさせない」をクリックします。55秒ごとにアイドルタイマーがリセットされます。"),
      ("Microsoft Teams の規約に違反しますか？", "ScreenWakeUp は画面のスリープを防ぎ、アイドルタイマーを止めるだけです。Teams・アカウント・社内データにはアクセスしません。所属組織のポリシーに従ってください。"),
      ("管理者権限なしで動きますか？", "はい。ブラウザのタブ内で動作し、インストールや管理者権限は不要です。")],
)
CONTENT["prevent-teams-away"]["ru"] = dict(
 title="Как избежать статуса «Нет на месте» в Teams (оставаться зелёным) — Бесплатно, без установки | ScreenWakeUp",
 desc="Не дайте Microsoft Teams показывать вас как «Нет на месте». Сохраняйте зелёный статус, не двигая мышью — бесплатный веб-инструмент, без загрузок и прав администратора. Работает на Windows, Mac и Chromebook.",
 keywords="избежать нет на месте teams, держать teams активным, зелёный статус teams, teams нет на месте 5 минут, оставаться активным в teams, двигать мышь автоматически",
 ogtitle="Как избежать статуса «Нет на месте» в Teams — оставаться зелёным без движения мышью",
 ogdesc="Бесплатный веб-инструмент, который сохраняет статус Microsoft Teams «Активен». Без загрузок и прав администратора.",
 tag="Microsoft Teams", h1='Как избежать <span>статуса «Нет на месте» в Teams</span>',
 lead="Сохраняйте статус Microsoft Teams зелёным и активным — не двигая мышью, ничего не устанавливая и без прав администратора.",
 body="""<p>Если Teams переключает вас в <strong>«Нет на месте»</strong>, стоит вам отойти почитать, ответить на звонок или сосредоточиться на другом окне, — вы не одиноки. Teams считывает <strong>таймер бездействия</strong> вашей операционной системы: примерно через 5 минут без мыши и клавиатуры — или когда экран блокируется или засыпает — он меняет ваш статус на «Нет на месте».</p>
  <div class="box"><strong>Решение в одну строку:</strong> сбрасывайте таймер бездействия системы (и держите экран активным) из вкладки браузера. Именно это делает ScreenWakeUp: бесплатно, в браузере, без установки.</div>
  <h2>Держите Teams активным за 3 шага</h2>
  <ol>
    <li><strong>Откройте инструмент.</strong> Перейдите на <a class="inline" href="{HOME}">screenwakeup.com</a> в Chrome или Edge в отдельной вкладке.</li>
    <li><strong>Включите анти-бездействие.</strong> Включите <strong>Имитировать движение мыши</strong> и <strong>Отправлять тихую клавишу F15</strong>.</li>
    <li><strong>Нажмите «Держать экран активным».</strong> Оставьте вкладку открытой и видимой. Статус остаётся зелёным, пока вкладка работает.</li>
  </ol>
  <h2>Почему Teams показывает меня как «Нет на месте»?</h2>
  <p>Teams определяет ваш статус по <strong>времени бездействия системы</strong> и <strong>состоянию экрана</strong>. ScreenWakeUp решает обе задачи сразу: удерживает блокировку экрана <em>и</em> каждые 55 секунд отправляет тихую клавишу <strong>F15</strong> плюс крошечное движение указателя.</p>
  <h2>Почему не настольное приложение «двигатель мыши»?</h2>
  <ul>
    <li><strong>Без установки и прав администратора</strong> — работает на корпоративных ноутбуках.</li>
    <li><strong>Ничего не хранит на вашем устройстве</strong> — работает во вкладке.</li>
    <li><strong>Кроссплатформенность</strong> — Windows, macOS и Chromebook.</li>
    <li><strong>Бесплатно, без аккаунта</strong> — а ещё это таймер Pomodoro и полноэкранные часы.</li>
  </ul>
  <h2>Частые вопросы</h2>
  <h3>Это нарушает правила Microsoft Teams?</h3>
  <p>ScreenWakeUp никогда не обращается к Teams, вашему аккаунту или данным компании: он лишь не даёт экрану заснуть и таймеру бездействия сработать. Всегда соблюдайте политику вашей организации.</p>
  <h3>Работает ли без прав администратора?</h3>
  <p>Да. Это просто веб-страница, ничего устанавливать не нужно.</p>
  <h3>Работает ли со Slack и Zoom?</h3>
  <p>Да. Тот же метод сохраняет Slack активным и не даёт Zoom пометить вас как неактивного.</p>""",
 cta="Оставайтесь зелёным в Teams → откройте бесплатный инструмент",
 related=[("Бесплатная замена Caffeine", "caffeine-alternative"), ("Держать экран iPhone активным", "keep-screen-awake-iphone")],
 bc_self="Избежать статуса «Нет на месте» в Teams",
 howto=dict(name="Как избежать статуса «Нет на месте» в Microsoft Teams",
            desc="Сохраняйте статус Microsoft Teams зелёным и активным, не меняя мышь или настройки системы.",
            steps=[("Откройте инструмент", "Откройте screenwakeup.com в Chrome или Edge в отдельной вкладке."),
                   ("Включите анти-бездействие", "Включите «Имитировать движение мыши» и «Отправлять тихую клавишу F15»."),
                   ("Включите", "Нажмите «Держать экран активным» и оставьте вкладку открытой.")]),
 faq=[("Почему Teams показывает меня как «Нет на месте»?", "Microsoft Teams помечает вас как «Нет на месте» примерно через 5 минут без активности клавиатуры или мыши, либо когда компьютер блокируется или засыпает. Он считывает таймер бездействия системы."),
      ("Как сохранить статус Teams зелёным, не двигая мышью?", "Откройте screenwakeup.com, включите «Имитировать движение мыши» и «Отправлять тихую клавишу F15» и нажмите «Держать экран активным». Это сбрасывает таймер каждые 55 секунд."),
      ("Это нарушает правила Microsoft Teams?", "ScreenWakeUp лишь не даёт экрану заснуть и останавливает таймер бездействия. Он не обращается к Teams, вашему аккаунту или данным компании. Соблюдайте политику вашей организации."),
      ("Работает ли без прав администратора?", "Да. Он работает во вкладке браузера, без установки и прав администратора.")],
)

# ============================ caffeine-alternative ============================
CONTENT["caffeine-alternative"]["es"] = dict(
 title="Alternativa gratis a Caffeine — Online, sin descargas (Mac y Windows) | ScreenWakeUp",
 desc="Alternativa gratuita y online a la app Caffeine. Mantén despierta la pantalla de tu Mac o Windows desde el navegador — sin descargas, sin instalar, sin cuenta. Funciona en cualquier sistema.",
 keywords="alternativa caffeine, caffeine mac, caffeine windows, app caffeine gratis, mantener mac despierto online, amphetamine alternativa, caffeine online sin descargar",
 ogtitle="Alternativa gratis a Caffeine — Online, sin descargas",
 ogdesc="Mantén despierta la pantalla de tu Mac o Windows desde el navegador. Gratis, sin instalar, sin cuenta.",
 tag="Alternativa a Caffeine", h1='Una <span>alternativa a Caffeine</span> gratis y online',
 lead="¿Te gustaba Caffeine pero no quieres instalar nada? ScreenWakeUp hace lo mismo desde el navegador — en Mac, Windows, Linux, Chromebook y móviles. Sin descargas, sin cuenta, gratis para siempre.",
 body="""<p>La clásica app <strong>Caffeine</strong> (y sus parientes como <strong>Amphetamine</strong> en Mac) evita que el equipo se suspenda manteniéndolo "despierto". El problema: hay que instalar software, y en un equipo de trabajo restringido a menudo no puedes. ScreenWakeUp usa la moderna <strong>Screen Wake Lock API</strong> de Chrome, Edge y Safari para hacer exactamente lo mismo — desde una pestaña.</p>
  <div class="box"><strong>Pruébalo en 5 segundos:</strong> abre <a class="inline" href="{HOME}">screenwakeup.com</a>, elige una duración (o ∞) y pulsa <strong>Mantener pantalla activa</strong>.</div>
  <h2>ScreenWakeUp frente a la app de escritorio Caffeine</h2>
  <table>
    <tr><th>&nbsp;</th><th>ScreenWakeUp</th><th>Caffeine / apps de escritorio</th></tr>
    <tr><td>Instalación</td><td><strong>Ninguna — en el navegador</strong></td><td>Descargar e instalar</td></tr>
    <tr><td>Permisos de administrador</td><td><strong>No necesarios</strong></td><td>A menudo requeridos</td></tr>
    <tr><td>Funciona en</td><td><strong>Cualquier SO + móvil</strong></td><td>Una app por SO</td></tr>
    <tr><td>Temporizador personalizado</td><td><strong>Sí</strong></td><td>Limitado</td></tr>
    <tr><td>Pomodoro + reloj a pantalla completa</td><td><strong>Sí</strong></td><td>No</td></tr>
    <tr><td>Anti-inactividad para Teams/Slack</td><td><strong>Sí</strong></td><td>No</td></tr>
    <tr><td>Precio</td><td><strong>Gratis</strong></td><td>Gratis / de pago</td></tr>
  </table>
  <h2>Cómo mantener la pantalla activa (sin instalar)</h2>
  <ol>
    <li>Abre <a class="inline" href="{HOME}">screenwakeup.com</a> en cualquier navegador moderno.</li>
    <li>Elige cuánto tiempo: 30 min, 1h, 2h, 4h o ∞.</li>
    <li>Pulsa <strong>Mantener pantalla activa</strong> y deja la pestaña abierta.</li>
  </ol>
  <h2>Funciona en Mac y Windows</h2>
  <p>En <strong>macOS</strong>, ábrelo en Safari o Chrome — la pantalla sigue encendida sin tocar Ajustes del Sistema ni el Ahorro de energía. En <strong>Windows 10/11</strong>, ábrelo en Chrome o Edge — anula el tiempo de espera sin cambiar la configuración de energía.</p>
  <h2>Más que "caffeine"</h2>
  <p>Como es un kit completo, también tienes un <a class="inline" href="{HOME}">temporizador personalizado, modo Pomodoro 25/5 y reloj a pantalla completa</a>, y <a class="inline" href="/es/prevent-teams-away/">anti-inactividad para seguir Activo en Teams y Slack</a> — todo en la misma página gratis.</p>""",
 cta="Abre la alternativa gratis a Caffeine →",
 related=[("Evitar estado Ausente en Teams", "prevent-teams-away"), ("Mantener pantalla activa en iPhone", "keep-screen-awake-iphone")],
 bc_self="Alternativa a Caffeine",
 faq=[("¿Hay una alternativa online gratis a la app Caffeine?", "Sí. ScreenWakeUp es una alternativa gratuita y basada en navegador a la app de escritorio Caffeine. No hay nada que descargar ni instalar: abre screenwakeup.com y pulsa un botón. Usa la moderna Screen Wake Lock API y funciona en Mac, Windows, Linux y móvil."),
      ("¿En qué se diferencia de la app de escritorio Caffeine?", "Caffeine es una app que instalas en macOS o Windows. ScreenWakeUp hace lo mismo desde una pestaña — sin instalación, sin permisos de administrador, y funciona en todos los sistemas, incluidos Chromebook y teléfonos. Además añade temporizador personalizado, Pomodoro, reloj a pantalla completa y anti-inactividad para Teams y Slack."),
      ("¿La alternativa online a Caffeine funciona en Mac?", "Sí. Abre screenwakeup.com en Safari o Chrome en tu Mac y pulsa el botón. La pantalla sigue encendida sin tocar Ajustes del Sistema ni el Ahorro de energía, y la paras cuando quieras con un clic."),
      ("¿Es realmente gratis y sin cuenta?", "Sí — totalmente gratis, sin registro, sin cuenta, sin recopilar datos. Se ejecuta por completo en tu navegador.")],
)
CONTENT["caffeine-alternative"]["pt"] = dict(
 title="Alternativa grátis ao Caffeine — Online, sem download (Mac e Windows) | ScreenWakeUp",
 desc="Alternativa gratuita e online ao app Caffeine. Mantenha a tela do seu Mac ou Windows acordada pelo navegador — sem download, sem instalar, sem conta. Funciona em qualquer sistema.",
 keywords="alternativa caffeine, caffeine mac, caffeine windows, app caffeine grátis, manter mac acordado online, amphetamine alternativa, caffeine online sem baixar",
 ogtitle="Alternativa grátis ao Caffeine — Online, sem download",
 ogdesc="Mantenha a tela do seu Mac ou Windows acordada pelo navegador. Grátis, sem instalar, sem conta.",
 tag="Alternativa ao Caffeine", h1='Uma <span>alternativa ao Caffeine</span> grátis e online',
 lead="Gostava do Caffeine mas não quer instalar nada? O ScreenWakeUp faz o mesmo pelo navegador — em Mac, Windows, Linux, Chromebook e celulares. Sem download, sem conta, grátis para sempre.",
 body="""<p>O clássico app <strong>Caffeine</strong> (e parentes como o <strong>Amphetamine</strong> no Mac) impede o computador de suspender mantendo-o "acordado". O problema: você precisa instalar software, e num computador de trabalho restrito muitas vezes não pode. O ScreenWakeUp usa a moderna <strong>Screen Wake Lock API</strong> do Chrome, Edge e Safari para fazer exatamente o mesmo — a partir de uma aba.</p>
  <div class="box"><strong>Teste em 5 segundos:</strong> abra <a class="inline" href="{HOME}">screenwakeup.com</a>, escolha uma duração (ou ∞) e clique em <strong>Manter tela ativa</strong>.</div>
  <h2>ScreenWakeUp vs. o app de desktop Caffeine</h2>
  <table>
    <tr><th>&nbsp;</th><th>ScreenWakeUp</th><th>Caffeine / apps de desktop</th></tr>
    <tr><td>Instalação</td><td><strong>Nenhuma — no navegador</strong></td><td>Baixar e instalar</td></tr>
    <tr><td>Direitos de administrador</td><td><strong>Não precisa</strong></td><td>Muitas vezes exigidos</td></tr>
    <tr><td>Funciona em</td><td><strong>Qualquer SO + celular</strong></td><td>Um app por SO</td></tr>
    <tr><td>Timer personalizado</td><td><strong>Sim</strong></td><td>Limitado</td></tr>
    <tr><td>Pomodoro + relógio em tela cheia</td><td><strong>Sim</strong></td><td>Não</td></tr>
    <tr><td>Anti-inatividade para Teams/Slack</td><td><strong>Sim</strong></td><td>Não</td></tr>
    <tr><td>Preço</td><td><strong>Grátis</strong></td><td>Grátis / pago</td></tr>
  </table>
  <h2>Como manter a tela ativa (sem instalar)</h2>
  <ol>
    <li>Abra <a class="inline" href="{HOME}">screenwakeup.com</a> em qualquer navegador moderno.</li>
    <li>Escolha quanto tempo: 30 min, 1h, 2h, 4h ou ∞.</li>
    <li>Clique em <strong>Manter tela ativa</strong> e deixe a aba aberta.</li>
  </ol>
  <h2>Funciona em Mac e Windows</h2>
  <p>No <strong>macOS</strong>, abra no Safari ou Chrome — a tela fica acesa sem mexer nas Configurações do Sistema nem no Economizador de energia. No <strong>Windows 10/11</strong>, abra no Chrome ou Edge — ignora o tempo limite sem mudar as configurações de energia.</p>
  <h2>Mais que "caffeine"</h2>
  <p>Por ser um kit completo, você também tem um <a class="inline" href="{HOME}">timer personalizado, modo Pomodoro 25/5 e relógio em tela cheia</a>, e <a class="inline" href="/pt/prevent-teams-away/">anti-inatividade para ficar Ativo no Teams e Slack</a> — tudo na mesma página grátis.</p>""",
 cta="Abra a alternativa grátis ao Caffeine →",
 related=[("Evitar status Ausente no Teams", "prevent-teams-away"), ("Manter tela ativa no iPhone", "keep-screen-awake-iphone")],
 bc_self="Alternativa ao Caffeine",
 faq=[("Existe uma alternativa online grátis ao app Caffeine?", "Sim. O ScreenWakeUp é uma alternativa gratuita baseada em navegador ao app de desktop Caffeine. Não há nada para baixar nem instalar: abra screenwakeup.com e clique em um botão. Usa a moderna Screen Wake Lock API e funciona em Mac, Windows, Linux e celular."),
      ("Qual a diferença para o app de desktop Caffeine?", "O Caffeine é um app que você instala no macOS ou Windows. O ScreenWakeUp faz o mesmo a partir de uma aba — sem instalação, sem direitos de administrador, e funciona em todos os sistemas, incluindo Chromebook e telefones. Ainda adiciona timer personalizado, Pomodoro, relógio em tela cheia e anti-inatividade para Teams e Slack."),
      ("A alternativa online ao Caffeine funciona no Mac?", "Sim. Abra screenwakeup.com no Safari ou Chrome no seu Mac e clique no botão. A tela fica acesa sem mexer nas Configurações do Sistema nem no Economizador de energia, e você para quando quiser com um clique."),
      ("É realmente grátis e sem conta?", "Sim — totalmente grátis, sem cadastro, sem conta, sem coletar dados. Roda inteiramente no seu navegador.")],
)
CONTENT["caffeine-alternative"]["fr"] = dict(
 title="Alternative gratuite à Caffeine — En ligne, sans téléchargement (Mac et Windows) | ScreenWakeUp",
 desc="Alternative gratuite et en ligne à l'appli Caffeine. Gardez l'écran de votre Mac ou Windows allumé depuis le navigateur — sans téléchargement, sans installation, sans compte. Fonctionne sur tout système.",
 keywords="alternative caffeine, caffeine mac, caffeine windows, appli caffeine gratuite, garder mac allumé en ligne, amphetamine alternative, caffeine en ligne sans télécharger",
 ogtitle="Alternative gratuite à Caffeine — En ligne, sans téléchargement",
 ogdesc="Gardez l'écran de votre Mac ou Windows allumé depuis le navigateur. Gratuit, sans installation, sans compte.",
 tag="Alternative à Caffeine", h1='Une <span>alternative à Caffeine</span> gratuite et en ligne',
 lead="Vous aimiez Caffeine mais ne voulez rien installer ? ScreenWakeUp fait pareil depuis le navigateur — sur Mac, Windows, Linux, Chromebook et mobiles. Sans téléchargement, sans compte, gratuit pour toujours.",
 body="""<p>La célèbre appli <strong>Caffeine</strong> (et ses cousines comme <strong>Amphetamine</strong> sur Mac) empêche la mise en veille en gardant l'ordinateur « éveillé ». Le hic : il faut installer un logiciel, et sur un ordinateur de travail verrouillé c'est souvent impossible. ScreenWakeUp utilise la <strong>Screen Wake Lock API</strong> moderne de Chrome, Edge et Safari pour faire exactement la même chose — depuis un onglet.</p>
  <div class="box"><strong>Essayez en 5 secondes :</strong> ouvrez <a class="inline" href="{HOME}">screenwakeup.com</a>, choisissez une durée (ou ∞) et cliquez sur <strong>Garder l'écran éveillé</strong>.</div>
  <h2>ScreenWakeUp face à l'appli de bureau Caffeine</h2>
  <table>
    <tr><th>&nbsp;</th><th>ScreenWakeUp</th><th>Caffeine / applis de bureau</th></tr>
    <tr><td>Installation</td><td><strong>Aucune — dans le navigateur</strong></td><td>Télécharger et installer</td></tr>
    <tr><td>Droits administrateur</td><td><strong>Pas nécessaires</strong></td><td>Souvent requis</td></tr>
    <tr><td>Fonctionne sur</td><td><strong>Tout OS + mobile</strong></td><td>Une appli par OS</td></tr>
    <tr><td>Minuteur personnalisé</td><td><strong>Oui</strong></td><td>Limité</td></tr>
    <tr><td>Pomodoro + horloge plein écran</td><td><strong>Oui</strong></td><td>Non</td></tr>
    <tr><td>Anti-inactivité pour Teams/Slack</td><td><strong>Oui</strong></td><td>Non</td></tr>
    <tr><td>Prix</td><td><strong>Gratuit</strong></td><td>Gratuit / payant</td></tr>
  </table>
  <h2>Comment garder l'écran éveillé (sans installation)</h2>
  <ol>
    <li>Ouvrez <a class="inline" href="{HOME}">screenwakeup.com</a> dans un navigateur moderne.</li>
    <li>Choisissez la durée : 30 min, 1h, 2h, 4h ou ∞.</li>
    <li>Cliquez sur <strong>Garder l'écran éveillé</strong> et laissez l'onglet ouvert.</li>
  </ol>
  <h2>Fonctionne sur Mac et Windows</h2>
  <p>Sur <strong>macOS</strong>, ouvrez-le dans Safari ou Chrome — l'écran reste allumé sans toucher aux Réglages Système ni à l'économiseur d'énergie. Sur <strong>Windows 10/11</strong>, ouvrez-le dans Chrome ou Edge — il ignore la mise en veille sans changer les options d'alimentation.</p>
  <h2>Plus qu'un « caffeine »</h2>
  <p>Comme c'est une boîte à outils complète, vous avez aussi un <a class="inline" href="{HOME}">minuteur personnalisé, un mode Pomodoro 25/5 et une horloge plein écran</a>, ainsi que l'<a class="inline" href="/fr/prevent-teams-away/">anti-inactivité pour rester Actif sur Teams et Slack</a> — le tout sur la même page gratuite.</p>""",
 cta="Ouvrir l'alternative gratuite à Caffeine →",
 related=[("Éviter le statut Absent sur Teams", "prevent-teams-away"), ("Garder l'écran de l'iPhone allumé", "keep-screen-awake-iphone")],
 bc_self="Alternative à Caffeine",
 faq=[("Existe-t-il une alternative en ligne gratuite à l'appli Caffeine ?", "Oui. ScreenWakeUp est une alternative gratuite, dans le navigateur, à l'appli de bureau Caffeine. Rien à télécharger ni installer : ouvrez screenwakeup.com et cliquez sur un bouton. Il utilise la Screen Wake Lock API moderne et fonctionne sur Mac, Windows, Linux et mobile."),
      ("Quelle différence avec l'appli de bureau Caffeine ?", "Caffeine est une appli que vous installez sur macOS ou Windows. ScreenWakeUp fait pareil depuis un onglet — sans installation, sans droits administrateur, et sur tous les systèmes y compris Chromebook et téléphones. Il ajoute aussi un minuteur personnalisé, Pomodoro, une horloge plein écran et l'anti-inactivité pour Teams et Slack."),
      ("L'alternative en ligne à Caffeine fonctionne-t-elle sur Mac ?", "Oui. Ouvrez screenwakeup.com dans Safari ou Chrome sur votre Mac et cliquez sur le bouton. L'écran reste allumé sans toucher aux Réglages Système ni à l'économiseur d'énergie, et vous l'arrêtez quand vous voulez d'un clic."),
      ("Est-ce vraiment gratuit et sans compte ?", "Oui — entièrement gratuit, sans inscription, sans compte, sans collecte de données. Tout s'exécute dans votre navigateur.")],
)
CONTENT["caffeine-alternative"]["de"] = dict(
 title="Kostenlose Caffeine-Alternative — Online, ohne Download (Mac & Windows) | ScreenWakeUp",
 desc="Eine kostenlose Online-Alternative zur Caffeine-App. Halten Sie den Bildschirm Ihres Mac oder Windows-PCs über den Browser wach — ohne Download, ohne Installation, ohne Konto. Funktioniert auf jedem System.",
 keywords="caffeine alternative, caffeine mac, caffeine windows, caffeine app kostenlos, mac wach halten online, amphetamine alternative, caffeine online ohne download",
 ogtitle="Kostenlose Caffeine-Alternative — Online, ohne Download",
 ogdesc="Halten Sie den Bildschirm Ihres Mac oder Windows-PCs über den Browser wach. Kostenlos, ohne Installation, ohne Konto.",
 tag="Caffeine-Alternative", h1='Eine kostenlose Online-<span>Caffeine-Alternative</span>',
 lead="Sie mochten die Caffeine-App, wollen aber nichts installieren? ScreenWakeUp macht dasselbe im Browser — auf Mac, Windows, Linux, Chromebook und Handys. Ohne Download, ohne Konto, für immer kostenlos.",
 body="""<p>Die klassische <strong>Caffeine</strong>-App (und Verwandte wie <strong>Amphetamine</strong> auf dem Mac) verhindern den Ruhezustand, indem sie den Rechner "wach" halten. Der Haken: Man muss Software installieren, und auf einem gesperrten Arbeitsrechner geht das oft nicht. ScreenWakeUp nutzt die moderne <strong>Screen Wake Lock API</strong> in Chrome, Edge und Safari für genau dasselbe — aus einem Tab.</p>
  <div class="box"><strong>In 5 Sekunden testen:</strong> Öffnen Sie <a class="inline" href="{HOME}">screenwakeup.com</a>, wählen Sie eine Dauer (oder ∞) und klicken Sie auf <strong>Bildschirm wach halten</strong>.</div>
  <h2>ScreenWakeUp im Vergleich zur Caffeine-Desktop-App</h2>
  <table>
    <tr><th>&nbsp;</th><th>ScreenWakeUp</th><th>Caffeine / Desktop-Apps</th></tr>
    <tr><td>Installation</td><td><strong>Keine — im Browser</strong></td><td>Herunterladen & installieren</td></tr>
    <tr><td>Administratorrechte</td><td><strong>Nicht nötig</strong></td><td>Oft erforderlich</td></tr>
    <tr><td>Läuft auf</td><td><strong>Jedem OS + Mobil</strong></td><td>Eine App pro OS</td></tr>
    <tr><td>Eigener Timer</td><td><strong>Ja</strong></td><td>Begrenzt</td></tr>
    <tr><td>Pomodoro + Vollbild-Uhr</td><td><strong>Ja</strong></td><td>Nein</td></tr>
    <tr><td>Anti-Inaktivität für Teams/Slack</td><td><strong>Ja</strong></td><td>Nein</td></tr>
    <tr><td>Preis</td><td><strong>Kostenlos</strong></td><td>Kostenlos / kostenpflichtig</td></tr>
  </table>
  <h2>So halten Sie den Bildschirm wach (ohne Installation)</h2>
  <ol>
    <li>Öffnen Sie <a class="inline" href="{HOME}">screenwakeup.com</a> in einem modernen Browser.</li>
    <li>Wählen Sie die Dauer: 30 Min, 1 Std, 2 Std, 4 Std oder ∞.</li>
    <li>Klicken Sie auf <strong>Bildschirm wach halten</strong> und lassen Sie den Tab offen.</li>
  </ol>
  <h2>Funktioniert auf Mac und Windows</h2>
  <p>Unter <strong>macOS</strong> öffnen Sie es in Safari oder Chrome — der Bildschirm bleibt an, ohne die Systemeinstellungen oder den Energiesparmodus anzufassen. Unter <strong>Windows 10/11</strong> öffnen Sie es in Chrome oder Edge — es überschreibt das Bildschirm-Timeout, ohne die Energieoptionen zu ändern.</p>
  <h2>Mehr als nur "Caffeine"</h2>
  <p>Da es ein komplettes Toolkit ist, erhalten Sie auch einen <a class="inline" href="{HOME}">eigenen Timer, einen 25/5-Pomodoro-Modus und eine Vollbild-Uhr</a> sowie <a class="inline" href="/de/prevent-teams-away/">Anti-Inaktivität, um in Teams und Slack Aktiv zu bleiben</a> — alles auf derselben kostenlosen Seite.</p>""",
 cta="Kostenlose Caffeine-Alternative öffnen →",
 related=[("Teams-Status Abwesend verhindern", "prevent-teams-away"), ("iPhone-Bildschirm wach halten", "keep-screen-awake-iphone")],
 bc_self="Caffeine-Alternative",
 faq=[("Gibt es eine kostenlose Online-Alternative zur Caffeine-App?", "Ja. ScreenWakeUp ist eine kostenlose, browserbasierte Alternative zur Caffeine-Desktop-App. Es gibt nichts herunterzuladen oder zu installieren: Öffnen Sie screenwakeup.com und klicken Sie auf eine Schaltfläche. Es nutzt die moderne Screen Wake Lock API und funktioniert auf Mac, Windows, Linux und Mobilgeräten."),
      ("Was ist der Unterschied zur Caffeine-Desktop-App?", "Caffeine ist eine App, die Sie auf macOS oder Windows installieren. ScreenWakeUp macht dasselbe aus einem Tab — ohne Installation, ohne Administratorrechte, und auf jedem System inklusive Chromebook und Handys. Es bietet zusätzlich einen eigenen Timer, Pomodoro, eine Vollbild-Uhr und Anti-Inaktivität für Teams und Slack."),
      ("Funktioniert die Online-Caffeine-Alternative auf dem Mac?", "Ja. Öffnen Sie screenwakeup.com in Safari oder Chrome auf Ihrem Mac und klicken Sie auf die Schaltfläche. Der Bildschirm bleibt an, ohne die Systemeinstellungen oder den Energiesparmodus zu berühren, und Sie stoppen ihn jederzeit mit einem Klick."),
      ("Ist es wirklich kostenlos und ohne Konto?", "Ja — völlig kostenlos, ohne Anmeldung, ohne Konto, ohne Datenerfassung. Es läuft vollständig in Ihrem Browser.")],
)
CONTENT["caffeine-alternative"]["ja"] = dict(
 title="無料の Caffeine 代替ツール — オンライン・ダウンロード不要（Mac・Windows）| ScreenWakeUp",
 desc="Caffeine アプリの無料オンライン代替。Mac や Windows の画面をブラウザからスリープさせない — ダウンロード・インストール・アカウント不要。あらゆる OS で動作。",
 keywords="caffeine 代替, caffeine mac, caffeine windows, caffeine 無料, mac スリープさせない オンライン, amphetamine 代替, caffeine オンライン",
 ogtitle="無料の Caffeine 代替ツール — オンライン・ダウンロード不要",
 ogdesc="Mac や Windows の画面をブラウザからスリープさせない。無料・インストール不要・アカウント不要。",
 tag="Caffeine 代替", h1='無料でオンラインの<span> Caffeine 代替</span>',
 lead="Caffeine アプリは好きだけど何もインストールしたくない？ ScreenWakeUp はブラウザから同じことをします — Mac・Windows・Linux・Chromebook・スマホで。ダウンロード不要、アカウント不要、ずっと無料。",
 body="""<p>定番の <strong>Caffeine</strong> アプリ（Mac の <strong>Amphetamine</strong> など同類も）は、PC を「起こした」状態に保ってスリープを防ぎます。難点は、ソフトのインストールが必要で、制限された社用 PC では入れられないことが多い点。ScreenWakeUp は Chrome・Edge・Safari の最新の <strong>Screen Wake Lock API</strong> を使い、まったく同じことをタブから実現します。</p>
  <div class="box"><strong>5秒で試す:</strong> <a class="inline" href="{HOME}">screenwakeup.com</a> を開き、時間（または ∞）を選んで<strong>「画面をスリープさせない」</strong>をクリック。</div>
  <h2>ScreenWakeUp と Caffeine デスクトップアプリの比較</h2>
  <table>
    <tr><th>&nbsp;</th><th>ScreenWakeUp</th><th>Caffeine / デスクトップアプリ</th></tr>
    <tr><td>インストール</td><td><strong>不要 — ブラウザで動作</strong></td><td>ダウンロード＆インストール</td></tr>
    <tr><td>管理者権限</td><td><strong>不要</strong></td><td>必要なことが多い</td></tr>
    <tr><td>対応</td><td><strong>あらゆる OS ＋スマホ</strong></td><td>OS ごとに別アプリ</td></tr>
    <tr><td>カスタムタイマー</td><td><strong>あり</strong></td><td>限定的</td></tr>
    <tr><td>ポモドーロ＋全画面時計</td><td><strong>あり</strong></td><td>なし</td></tr>
    <tr><td>Teams/Slack のアイドル防止</td><td><strong>あり</strong></td><td>なし</td></tr>
    <tr><td>価格</td><td><strong>無料</strong></td><td>無料／有料</td></tr>
  </table>
  <h2>画面をスリープさせない手順（インストール不要）</h2>
  <ol>
    <li>最新のブラウザで <a class="inline" href="{HOME}">screenwakeup.com</a> を開きます。</li>
    <li>時間を選択：30分・1時間・2時間・4時間・∞。</li>
    <li><strong>「画面をスリープさせない」</strong>をクリックし、タブを開いたままにします。</li>
  </ol>
  <h2>Mac と Windows で動作</h2>
  <p><strong>macOS</strong> では Safari か Chrome で開くと、システム設定や省エネ設定を触らずに画面が点いたままになります。<strong>Windows 10/11</strong> では Chrome か Edge で開くと、電源設定を変えずに画面のタイムアウトを上書きします。</p>
  <h2>単なる「caffeine」以上</h2>
  <p>総合ツールなので、<a class="inline" href="{HOME}">カスタムタイマー・25/5 ポモドーロ・全画面時計</a>に加え、<a class="inline" href="/ja/prevent-teams-away/">Teams や Slack でアクティブを維持するアイドル防止</a>も同じ無料ページで使えます。</p>""",
 cta="無料の Caffeine 代替を開く →",
 related=[("Teams の退席中を防ぐ", "prevent-teams-away"), ("iPhone の画面をスリープさせない", "keep-screen-awake-iphone")],
 bc_self="Caffeine 代替",
 faq=[("Caffeine アプリの無料オンライン代替はありますか？", "はい。ScreenWakeUp は Caffeine デスクトップアプリの無料・ブラウザベースの代替です。ダウンロードやインストールは不要で、screenwakeup.com を開いてボタンを押すだけ。最新の Screen Wake Lock API を使い、Mac・Windows・Linux・モバイルで動作します。"),
      ("Caffeine デスクトップアプリとの違いは？", "Caffeine は macOS や Windows にインストールするアプリです。ScreenWakeUp はタブから同じことを行い、インストール不要・管理者権限不要で、Chromebook やスマホを含むあらゆる OS で動作します。さらにカスタムタイマー、ポモドーロ、全画面時計、Teams・Slack のアイドル防止も備えます。"),
      ("オンラインの Caffeine 代替は Mac で動きますか？", "はい。Mac の Safari か Chrome で screenwakeup.com を開いてボタンを押すだけ。システム設定や省エネ設定を触らずに画面が点いたままになり、ワンクリックでいつでも停止できます。"),
      ("本当に無料・アカウント不要ですか？", "はい — 完全無料、登録不要、アカウント不要、データ収集なし。すべてブラウザ内で動作します。")],
)
CONTENT["caffeine-alternative"]["ru"] = dict(
 title="Бесплатная замена Caffeine — Онлайн, без загрузки (Mac и Windows) | ScreenWakeUp",
 desc="Бесплатная онлайн-замена приложения Caffeine. Держите экран Mac или Windows активным прямо из браузера — без загрузки, без установки, без аккаунта. Работает на любой системе.",
 keywords="замена caffeine, caffeine mac, caffeine windows, caffeine бесплатно, держать mac активным онлайн, amphetamine замена, caffeine онлайн без загрузки",
 ogtitle="Бесплатная замена Caffeine — Онлайн, без загрузки",
 ogdesc="Держите экран Mac или Windows активным прямо из браузера. Бесплатно, без установки, без аккаунта.",
 tag="Замена Caffeine", h1='Бесплатная онлайн-<span>замена Caffeine</span>',
 lead="Нравился Caffeine, но не хотите ничего устанавливать? ScreenWakeUp делает то же из браузера — на Mac, Windows, Linux, Chromebook и телефонах. Без загрузки, без аккаунта, бесплатно навсегда.",
 body="""<p>Классическое приложение <strong>Caffeine</strong> (и его родственники вроде <strong>Amphetamine</strong> на Mac) не дают компьютеру заснуть, удерживая его «бодрствующим». Загвоздка: нужно устанавливать программу, а на корпоративном ноутбуке это часто невозможно. ScreenWakeUp использует современный <strong>Screen Wake Lock API</strong> в Chrome, Edge и Safari, чтобы делать ровно то же — прямо из вкладки.</p>
  <div class="box"><strong>Попробуйте за 5 секунд:</strong> откройте <a class="inline" href="{HOME}">screenwakeup.com</a>, выберите длительность (или ∞) и нажмите <strong>Держать экран активным</strong>.</div>
  <h2>ScreenWakeUp против настольного приложения Caffeine</h2>
  <table>
    <tr><th>&nbsp;</th><th>ScreenWakeUp</th><th>Caffeine / настольные приложения</th></tr>
    <tr><td>Установка</td><td><strong>Не нужна — в браузере</strong></td><td>Скачать и установить</td></tr>
    <tr><td>Права администратора</td><td><strong>Не нужны</strong></td><td>Часто требуются</td></tr>
    <tr><td>Работает на</td><td><strong>Любой ОС + мобильные</strong></td><td>Одно приложение на ОС</td></tr>
    <tr><td>Свой таймер</td><td><strong>Да</strong></td><td>Ограниченно</td></tr>
    <tr><td>Pomodoro + полноэкранные часы</td><td><strong>Да</strong></td><td>Нет</td></tr>
    <tr><td>Анти-бездействие для Teams/Slack</td><td><strong>Да</strong></td><td>Нет</td></tr>
    <tr><td>Цена</td><td><strong>Бесплатно</strong></td><td>Бесплатно / платно</td></tr>
  </table>
  <h2>Как держать экран активным (без установки)</h2>
  <ol>
    <li>Откройте <a class="inline" href="{HOME}">screenwakeup.com</a> в любом современном браузере.</li>
    <li>Выберите время: 30 мин, 1 ч, 2 ч, 4 ч или ∞.</li>
    <li>Нажмите <strong>Держать экран активным</strong> и оставьте вкладку открытой.</li>
  </ol>
  <h2>Работает на Mac и Windows</h2>
  <p>На <strong>macOS</strong> откройте в Safari или Chrome — экран остаётся включённым, не трогая Системные настройки или Экономию энергии. На <strong>Windows 10/11</strong> откройте в Chrome или Edge — переопределяет тайм-аут экрана, не меняя настройки электропитания.</p>
  <h2>Больше, чем просто «caffeine»</h2>
  <p>Это полноценный набор инструментов, поэтому вы также получаете <a class="inline" href="{HOME}">свой таймер, режим Pomodoro 25/5 и полноэкранные часы</a>, а ещё <a class="inline" href="/ru/prevent-teams-away/">анти-бездействие, чтобы оставаться активным в Teams и Slack</a> — всё на одной бесплатной странице.</p>""",
 cta="Открыть бесплатную замену Caffeine →",
 related=[("Избежать статуса «Нет на месте» в Teams", "prevent-teams-away"), ("Держать экран iPhone активным", "keep-screen-awake-iphone")],
 bc_self="Замена Caffeine",
 faq=[("Есть ли бесплатная онлайн-замена приложению Caffeine?", "Да. ScreenWakeUp — бесплатная браузерная замена настольному приложению Caffeine. Ничего скачивать и устанавливать не нужно: откройте screenwakeup.com и нажмите кнопку. Он использует современный Screen Wake Lock API и работает на Mac, Windows, Linux и мобильных."),
      ("Чем он отличается от настольного приложения Caffeine?", "Caffeine — приложение, которое вы устанавливаете на macOS или Windows. ScreenWakeUp делает то же из вкладки — без установки, без прав администратора, и на любой системе, включая Chromebook и телефоны. Также добавляет свой таймер, Pomodoro, полноэкранные часы и анти-бездействие для Teams и Slack."),
      ("Работает ли онлайн-замена Caffeine на Mac?", "Да. Откройте screenwakeup.com в Safari или Chrome на Mac и нажмите кнопку. Экран остаётся включённым, не трогая Системные настройки или Экономию энергии, и вы останавливаете его одним кликом в любой момент."),
      ("Это действительно бесплатно и без аккаунта?", "Да — полностью бесплатно, без регистрации, без аккаунта, без сбора данных. Всё работает в вашем браузере.")],
)

# ============================ keep-screen-awake-iphone ============================
CONTENT["keep-screen-awake-iphone"]["es"] = dict(
 title="Cómo mantener la pantalla del iPhone encendida — Gratis, sin app (iOS y iPad) | ScreenWakeUp",
 desc="Evita que la pantalla de tu iPhone o iPad se apague — sin cambiar el Bloqueo automático ni instalar apps. Herramienta web gratis que funciona en Safari y Chrome en iOS 16.4+.",
 keywords="mantener pantalla iphone encendida, pantalla iphone no se apaga, evitar bloqueo automatico iphone, ipad pantalla activa, mantener pantalla ios, pantalla iphone siempre encendida",
 ogtitle="Cómo mantener la pantalla del iPhone encendida — Gratis, sin app",
 ogdesc="Mantén encendida la pantalla de tu iPhone o iPad desde Safari. Sin app, sin tocar el Bloqueo automático. Gratis.",
 tag="iPhone y iPad", h1='Cómo mantener la <span>pantalla del iPhone encendida</span>',
 lead="Evita que la pantalla de tu iPhone o iPad se apague — sin cambiar el Bloqueo automático y sin instalar ninguna app. Funciona directamente en Safari, gratis.",
 body="""<p>¿Lees una receta, sigues una partitura, escaneas un menú QR o ves un documento en el móvil? iOS atenúa y bloquea la pantalla tras el tiempo de <strong>Bloqueo automático</strong>. Puedes entrar en Ajustes cada vez — o abrir ScreenWakeUp, que usa la <strong>Screen Wake Lock API</strong> (iOS 16.4+) para mantener la pantalla encendida mientras la pestaña esté abierta.</p>
  <div class="box"><strong>Versión rápida:</strong> abre <a class="inline" href="{HOME}">screenwakeup.com</a> en Safari → toca <strong>Mantener pantalla activa</strong> → deja la pestaña visible. Listo.</div>
  <h2>Mantén la pantalla del iPhone encendida en 3 pasos</h2>
  <ol>
    <li>Abre <a class="inline" href="{HOME}">screenwakeup.com</a> en <strong>Safari</strong> en tu iPhone o iPad.</li>
    <li>Elige una duración — 30 min, 1h, 2h, 4h o ∞.</li>
    <li>Toca <strong>Mantener pantalla activa</strong> y deja la pestaña de Safari abierta y a la vista.</li>
  </ol>
  <p>Truco: añádelo a la pantalla de inicio (Compartir → Añadir a pantalla de inicio) para abrirlo como una app.</p>
  <h2>¿Por qué no cambiar el Bloqueo automático?</h2>
  <p>Puedes poner <em>Ajustes &gt; Pantalla y brillo &gt; Bloqueo automático &gt; Nunca</em> — pero entonces la pantalla <strong>nunca</strong> se bloquea, gasta batería y deja el teléfono desbloqueado todo el día. ScreenWakeUp mantiene la pantalla encendida solo cuando lo necesitas; al cerrar la pestaña, todo vuelve a la normalidad.</p>
  <h2>Qué necesitas</h2>
  <ul>
    <li><strong>iOS / iPadOS 16.4 o posterior</strong> para la Wake Lock API nativa en Safari.</li>
    <li>La pestaña debe permanecer <strong>abierta y visible</strong> — si cambias de app o bloqueas el teléfono, iOS libera el bloqueo y lo recupera al volver.</li>
  </ul>
  <h2>Preguntas frecuentes</h2>
  <h3>¿Funciona en iPad?</h3>
  <p>Sí, igual — Safari o Chrome en iPadOS. Perfecto para recetas, presentaciones y pantallas tipo kiosco.</p>
  <h3>¿Gasta batería?</h3>
  <p>Mantener cualquier pantalla encendida consume energía, pero solo mientras la pestaña está activa. Al cerrarla vuelve el Bloqueo automático normal, mucho más seguro que ponerlo en Nunca.</p>""",
 cta="Mantén tu iPhone encendido → abre la herramienta",
 related=[("Evitar estado Ausente en Teams", "prevent-teams-away"), ("Alternativa gratis a Caffeine", "caffeine-alternative")],
 bc_self="Mantener pantalla del iPhone encendida",
 howto=dict(name="Cómo mantener la pantalla del iPhone encendida",
            desc="Mantén encendida la pantalla de tu iPhone o iPad sin cambiar el Bloqueo automático ni instalar una app.",
            steps=[("Abre en Safari", "Abre screenwakeup.com en Safari en tu iPhone o iPad (iOS 16.4 o posterior)."),
                   ("Elige una duración", "Elige cuánto tiempo quieres la pantalla encendida, o ∞."),
                   ("Toca Mantener pantalla activa", "Toca el botón y deja la pestaña de Safari abierta y visible.")]),
 faq=[("¿Cómo mantengo la pantalla del iPhone encendida sin cambiar el Bloqueo automático?", "Abre screenwakeup.com en Safari y toca 'Mantener pantalla activa'. Usa la Screen Wake Lock API (iOS 16.4+) para mantener la pantalla encendida mientras la pestaña está abierta, sin tocar Ajustes > Pantalla y brillo > Bloqueo automático."),
      ("¿Funciona también en iPad?", "Sí. Funciona igual en iPadOS en Safari o Chrome. Mantén la pestaña abierta y a la vista."),
      ("¿Qué versión de iOS necesito?", "iOS y iPadOS 16.4 o posterior admiten la Screen Wake Lock API en Safari. En versiones anteriores usa un método alternativo, aunque es más fiable en 16.4+."),
      ("¿Por qué la pantalla se atenúa al bloquear el teléfono o cambiar de app?", "El bloqueo de pantalla solo funciona mientras la pestaña está abierta y visible. Si cambias de app o bloqueas el teléfono, iOS lo libera. Vuelve a la pestaña y se reactiva automáticamente.")],
)
CONTENT["keep-screen-awake-iphone"]["pt"] = dict(
 title="Como manter a tela do iPhone ligada — Grátis, sem app (iOS e iPad) | ScreenWakeUp",
 desc="Impeça a tela do seu iPhone ou iPad de apagar — sem mudar o Bloqueio automático nem instalar apps. Ferramenta web grátis que funciona no Safari e Chrome no iOS 16.4+.",
 keywords="manter tela iphone ligada, tela iphone não apaga, evitar bloqueio automatico iphone, ipad tela ativa, manter tela ios, tela iphone sempre ligada",
 ogtitle="Como manter a tela do iPhone ligada — Grátis, sem app",
 ogdesc="Mantenha a tela do seu iPhone ou iPad ligada pelo Safari. Sem app, sem mexer no Bloqueio automático. Grátis.",
 tag="iPhone e iPad", h1='Como manter a <span>tela do iPhone ligada</span>',
 lead="Impeça a tela do seu iPhone ou iPad de apagar — sem mudar o Bloqueio automático e sem instalar nenhum app. Funciona direto no Safari, grátis.",
 body="""<p>Lendo uma receita, seguindo uma partitura, escaneando um cardápio QR ou vendo um documento no celular? O iOS escurece e bloqueia a tela após o tempo de <strong>Bloqueio automático</strong>. Você pode entrar nos Ajustes toda vez — ou abrir o ScreenWakeUp, que usa a <strong>Screen Wake Lock API</strong> (iOS 16.4+) para manter a tela ligada enquanto a aba estiver aberta.</p>
  <div class="box"><strong>Versão rápida:</strong> abra <a class="inline" href="{HOME}">screenwakeup.com</a> no Safari → toque em <strong>Manter tela ativa</strong> → deixe a aba visível. Pronto.</div>
  <h2>Mantenha a tela do iPhone ligada em 3 passos</h2>
  <ol>
    <li>Abra <a class="inline" href="{HOME}">screenwakeup.com</a> no <strong>Safari</strong> no seu iPhone ou iPad.</li>
    <li>Escolha uma duração — 30 min, 1h, 2h, 4h ou ∞.</li>
    <li>Toque em <strong>Manter tela ativa</strong> e deixe a aba do Safari aberta e visível.</li>
  </ol>
  <p>Dica: adicione à Tela de Início (Compartilhar → Adicionar à Tela de Início) para abrir como um app.</p>
  <h2>Por que não mudar o Bloqueio automático?</h2>
  <p>Você pode definir <em>Ajustes &gt; Tela e Brilho &gt; Bloqueio Automático &gt; Nunca</em> — mas aí a tela <strong>nunca</strong> bloqueia, gasta bateria e deixa o telefone desbloqueado o dia todo. O ScreenWakeUp mantém a tela ligada só quando você precisa; ao fechar a aba, tudo volta ao normal.</p>
  <h2>O que você precisa</h2>
  <ul>
    <li><strong>iOS / iPadOS 16.4 ou posterior</strong> para a Wake Lock API nativa no Safari.</li>
    <li>A aba precisa ficar <strong>aberta e visível</strong> — se você trocar de app ou bloquear o telefone, o iOS libera o bloqueio e o recupera ao voltar.</li>
  </ul>
  <h2>Perguntas frequentes</h2>
  <h3>Funciona no iPad?</h3>
  <p>Sim, igual — Safari ou Chrome no iPadOS. Ótimo para receitas, apresentações e telas tipo quiosque.</p>
  <h3>Gasta bateria?</h3>
  <p>Manter qualquer tela ligada consome energia, mas só enquanto a aba está ativa. Ao fechá-la, o Bloqueio automático normal volta, bem mais seguro que deixar em Nunca.</p>""",
 cta="Mantenha seu iPhone ligado → abra a ferramenta",
 related=[("Evitar status Ausente no Teams", "prevent-teams-away"), ("Alternativa grátis ao Caffeine", "caffeine-alternative")],
 bc_self="Manter tela do iPhone ligada",
 howto=dict(name="Como manter a tela do iPhone ligada",
            desc="Mantenha a tela do seu iPhone ou iPad ligada sem mudar o Bloqueio automático nem instalar um app.",
            steps=[("Abra no Safari", "Abra screenwakeup.com no Safari no seu iPhone ou iPad (iOS 16.4 ou posterior)."),
                   ("Escolha uma duração", "Escolha por quanto tempo a tela deve ficar ligada, ou ∞."),
                   ("Toque em Manter tela ativa", "Toque no botão e deixe a aba do Safari aberta e visível.")]),
 faq=[("Como mantenho a tela do iPhone ligada sem mudar o Bloqueio automático?", "Abra screenwakeup.com no Safari e toque em 'Manter tela ativa'. Usa a Screen Wake Lock API (iOS 16.4+) para manter a tela ligada enquanto a aba está aberta, sem mexer em Ajustes > Tela e Brilho > Bloqueio Automático."),
      ("Funciona também no iPad?", "Sim. Funciona igual no iPadOS no Safari ou Chrome. Mantenha a aba aberta e visível."),
      ("Qual versão do iOS preciso?", "iOS e iPadOS 16.4 ou posterior suportam a Screen Wake Lock API no Safari. Em versões anteriores usa um método alternativo, embora seja mais confiável no 16.4+."),
      ("Por que a tela ainda escurece quando bloqueio o telefone ou troco de app?", "O bloqueio de tela só funciona enquanto a aba está aberta e visível. Se você trocar de app ou bloquear o telefone, o iOS o libera. Volte à aba e ele reativa automaticamente.")],
)
CONTENT["keep-screen-awake-iphone"]["fr"] = dict(
 title="Comment garder l'écran de l'iPhone allumé — Gratuit, sans appli (iOS et iPad) | ScreenWakeUp",
 desc="Empêchez l'écran de votre iPhone ou iPad de s'éteindre — sans changer le Verrouillage automatique ni installer d'appli. Outil web gratuit qui fonctionne dans Safari et Chrome sur iOS 16.4+.",
 keywords="garder écran iphone allumé, écran iphone ne s'éteint pas, éviter verrouillage automatique iphone, ipad écran allumé, garder écran ios, écran iphone toujours allumé",
 ogtitle="Comment garder l'écran de l'iPhone allumé — Gratuit, sans appli",
 ogdesc="Gardez l'écran de votre iPhone ou iPad allumé depuis Safari. Sans appli, sans toucher au Verrouillage automatique. Gratuit.",
 tag="iPhone et iPad", h1="Comment garder l'<span>écran de l'iPhone allumé</span>",
 lead="Empêchez l'écran de votre iPhone ou iPad de s'éteindre — sans changer le Verrouillage automatique et sans installer d'appli. Ça marche directement dans Safari, gratuitement.",
 body="""<p>Vous lisez une recette, suivez une partition, scannez un menu QR ou regardez un document sur le téléphone ? iOS atténue et verrouille l'écran après le délai de <strong>Verrouillage automatique</strong>. Vous pourriez fouiller dans les Réglages à chaque fois — ou ouvrir ScreenWakeUp, qui utilise la <strong>Screen Wake Lock API</strong> (iOS 16.4+) pour garder l'écran allumé tant que l'onglet est ouvert.</p>
  <div class="box"><strong>Version rapide :</strong> ouvrez <a class="inline" href="{HOME}">screenwakeup.com</a> dans Safari → touchez <strong>Garder l'écran éveillé</strong> → laissez l'onglet visible. C'est fait.</div>
  <h2>Gardez l'écran de l'iPhone allumé en 3 étapes</h2>
  <ol>
    <li>Ouvrez <a class="inline" href="{HOME}">screenwakeup.com</a> dans <strong>Safari</strong> sur votre iPhone ou iPad.</li>
    <li>Choisissez une durée — 30 min, 1h, 2h, 4h ou ∞.</li>
    <li>Touchez <strong>Garder l'écran éveillé</strong> et laissez l'onglet Safari ouvert et visible.</li>
  </ol>
  <p>Astuce : ajoutez-le à l'écran d'accueil (Partager → Sur l'écran d'accueil) pour l'ouvrir comme une appli.</p>
  <h2>Pourquoi ne pas juste changer le Verrouillage automatique ?</h2>
  <p>Vous pouvez régler <em>Réglages &gt; Luminosité et affichage &gt; Verrouillage auto &gt; Jamais</em> — mais alors l'écran ne se verrouille <strong>jamais</strong>, vide la batterie et laisse le téléphone déverrouillé toute la journée. ScreenWakeUp garde l'écran allumé seulement quand vous en avez besoin ; à la fermeture de l'onglet, tout revient à la normale.</p>
  <h2>Ce qu'il vous faut</h2>
  <ul>
    <li><strong>iOS / iPadOS 16.4 ou ultérieur</strong> pour la Wake Lock API native dans Safari.</li>
    <li>L'onglet doit rester <strong>ouvert et visible</strong> — si vous changez d'appli ou verrouillez le téléphone, iOS libère le verrou et le réacquiert à votre retour.</li>
  </ul>
  <h2>Questions fréquentes</h2>
  <h3>Fonctionne-t-il sur iPad ?</h3>
  <p>Oui, à l'identique — Safari ou Chrome sur iPadOS. Parfait pour les recettes, présentations et écrans de type kiosque.</p>
  <h3>Cela vide-t-il la batterie ?</h3>
  <p>Garder un écran allumé consomme de l'énergie, mais seulement tant que l'onglet est actif. À sa fermeture, le Verrouillage automatique normal reprend, bien plus sûr que de le mettre sur Jamais.</p>""",
 cta="Gardez votre iPhone allumé → ouvrez l'outil",
 related=[("Éviter le statut Absent sur Teams", "prevent-teams-away"), ("Alternative gratuite à Caffeine", "caffeine-alternative")],
 bc_self="Garder l'écran de l'iPhone allumé",
 howto=dict(name="Comment garder l'écran de l'iPhone allumé",
            desc="Gardez l'écran de votre iPhone ou iPad allumé sans changer le Verrouillage automatique ni installer d'appli.",
            steps=[("Ouvrez dans Safari", "Ouvrez screenwakeup.com dans Safari sur votre iPhone ou iPad (iOS 16.4 ou ultérieur)."),
                   ("Choisissez une durée", "Choisissez combien de temps l'écran doit rester allumé, ou ∞."),
                   ("Touchez Garder l'écran éveillé", "Touchez le bouton et laissez l'onglet Safari ouvert et visible.")]),
 faq=[("Comment garder l'écran de l'iPhone allumé sans changer le Verrouillage automatique ?", "Ouvrez screenwakeup.com dans Safari et touchez 'Garder l'écran éveillé'. Il utilise la Screen Wake Lock API (iOS 16.4+) pour garder l'écran allumé tant que l'onglet est ouvert, sans toucher à Réglages > Luminosité et affichage > Verrouillage auto."),
      ("Fonctionne-t-il aussi sur iPad ?", "Oui. Cela fonctionne de la même façon sur iPadOS dans Safari ou Chrome. Gardez l'onglet ouvert et visible."),
      ("Quelle version d'iOS faut-il ?", "iOS et iPadOS 16.4 ou ultérieur prennent en charge la Screen Wake Lock API dans Safari. Sur les versions plus anciennes, une méthode de secours est utilisée, mais c'est plus fiable sur 16.4+."),
      ("Pourquoi l'écran s'atténue-t-il quand je verrouille le téléphone ou change d'appli ?", "Le verrou d'écran ne fonctionne que tant que l'onglet est ouvert et visible. Si vous changez d'appli ou verrouillez le téléphone, iOS le libère. Revenez à l'onglet et il se réactive automatiquement.")],
)
CONTENT["keep-screen-awake-iphone"]["de"] = dict(
 title="iPhone-Bildschirm anlassen — Kostenlos, ohne App (iOS & iPad) | ScreenWakeUp",
 desc="Verhindern Sie, dass sich der Bildschirm Ihres iPhones oder iPads ausschaltet — ohne die automatische Sperre zu ändern oder eine App zu installieren. Kostenloses Web-Tool für Safari und Chrome unter iOS 16.4+.",
 keywords="iphone bildschirm anlassen, iphone bildschirm geht aus, automatische sperre iphone verhindern, ipad bildschirm an, bildschirm wach halten ios, iphone display immer an",
 ogtitle="iPhone-Bildschirm anlassen — Kostenlos, ohne App",
 ogdesc="Halten Sie den Bildschirm Ihres iPhones oder iPads über Safari an. Ohne App, ohne die automatische Sperre zu ändern. Kostenlos.",
 tag="iPhone & iPad", h1='So lassen Sie den <span>iPhone-Bildschirm an</span>',
 lead="Verhindern Sie, dass sich der Bildschirm Ihres iPhones oder iPads ausschaltet — ohne die automatische Sperre zu ändern und ohne App. Läuft direkt in Safari, kostenlos.",
 body="""<p>Sie lesen ein Rezept, folgen Noten, scannen eine QR-Speisekarte oder schauen ein Dokument auf dem Handy? iOS dimmt und sperrt den Bildschirm nach der <strong>automatischen Sperre</strong>. Sie könnten jedes Mal in die Einstellungen gehen — oder ScreenWakeUp öffnen, das die <strong>Screen Wake Lock API</strong> (iOS 16.4+) nutzt, um den Bildschirm anzulassen, solange der Tab offen ist.</p>
  <div class="box"><strong>Kurzfassung:</strong> Öffnen Sie <a class="inline" href="{HOME}">screenwakeup.com</a> in Safari → tippen Sie auf <strong>Bildschirm wach halten</strong> → lassen Sie den Tab sichtbar. Fertig.</div>
  <h2>iPhone-Bildschirm in 3 Schritten anlassen</h2>
  <ol>
    <li>Öffnen Sie <a class="inline" href="{HOME}">screenwakeup.com</a> in <strong>Safari</strong> auf Ihrem iPhone oder iPad.</li>
    <li>Wählen Sie eine Dauer — 30 Min, 1 Std, 2 Std, 4 Std oder ∞.</li>
    <li>Tippen Sie auf <strong>Bildschirm wach halten</strong> und lassen Sie den Safari-Tab offen und sichtbar.</li>
  </ol>
  <p>Tipp: Zum Home-Bildschirm hinzufügen (Teilen → Zum Home-Bildschirm) und wie eine App öffnen.</p>
  <h2>Warum nicht einfach die automatische Sperre ändern?</h2>
  <p>Sie können <em>Einstellungen &gt; Anzeige & Helligkeit &gt; Automatische Sperre &gt; Nie</em> setzen — dann sperrt der Bildschirm aber <strong>nie</strong>, verbraucht Akku und lässt das Handy den ganzen Tag entsperrt. ScreenWakeUp hält den Bildschirm nur an, wenn Sie es brauchen; beim Schließen des Tabs ist alles wieder normal.</p>
  <h2>Was Sie brauchen</h2>
  <ul>
    <li><strong>iOS / iPadOS 16.4 oder neuer</strong> für die native Wake Lock API in Safari.</li>
    <li>Der Tab muss <strong>offen und sichtbar</strong> bleiben — wechseln Sie die App oder sperren Sie das Handy, gibt iOS die Sperre frei und holt sie bei der Rückkehr zurück.</li>
  </ul>
  <h2>Häufige Fragen</h2>
  <h3>Funktioniert es auf dem iPad?</h3>
  <p>Ja, identisch — Safari oder Chrome unter iPadOS. Ideal für Rezepte, Präsentationen und Kiosk-Displays.</p>
  <h3>Verbraucht es Akku?</h3>
  <p>Jeden Bildschirm anzulassen kostet Energie, aber nur solange der Tab aktiv ist. Beim Schließen kehrt die normale automatische Sperre zurück — viel sicherer als „Nie".</p>""",
 cta="iPhone anlassen → Tool öffnen",
 related=[("Teams-Status Abwesend verhindern", "prevent-teams-away"), ("Kostenlose Caffeine-Alternative", "caffeine-alternative")],
 bc_self="iPhone-Bildschirm anlassen",
 howto=dict(name="So lassen Sie den iPhone-Bildschirm an",
            desc="Halten Sie den Bildschirm Ihres iPhones oder iPads an, ohne die automatische Sperre zu ändern oder eine App zu installieren.",
            steps=[("In Safari öffnen", "Öffnen Sie screenwakeup.com in Safari auf Ihrem iPhone oder iPad (iOS 16.4 oder neuer)."),
                   ("Dauer wählen", "Wählen Sie, wie lange der Bildschirm anbleiben soll, oder ∞."),
                   ("Bildschirm wach halten tippen", "Tippen Sie auf die Schaltfläche und lassen Sie den Safari-Tab offen und sichtbar.")]),
 faq=[("Wie lasse ich den iPhone-Bildschirm an, ohne die automatische Sperre zu ändern?", "Öffnen Sie screenwakeup.com in Safari und tippen Sie auf 'Bildschirm wach halten'. Es nutzt die Screen Wake Lock API (iOS 16.4+), um den Bildschirm anzulassen, solange der Tab offen ist — ohne Einstellungen > Anzeige & Helligkeit > Automatische Sperre zu ändern."),
      ("Funktioniert es auch auf dem iPad?", "Ja. Es funktioniert genauso unter iPadOS in Safari oder Chrome. Lassen Sie den Tab offen und sichtbar."),
      ("Welche iOS-Version brauche ich?", "iOS und iPadOS 16.4 oder neuer unterstützen die Screen Wake Lock API in Safari. Auf älteren Versionen wird eine Ausweichmethode genutzt, am zuverlässigsten ist es ab 16.4."),
      ("Warum dimmt der Bildschirm trotzdem, wenn ich das Handy sperre oder die App wechsle?", "Die Bildschirmsperre wirkt nur, solange der Tab offen und sichtbar ist. Wechseln Sie die App oder sperren das Handy, gibt iOS sie frei. Kehren Sie zum Tab zurück, aktiviert sie sich automatisch.")],
)
CONTENT["keep-screen-awake-iphone"]["ja"] = dict(
 title="iPhone の画面をスリープさせない方法 — 無料・アプリ不要（iOS・iPad）| ScreenWakeUp",
 desc="iPhone や iPad の画面が消えないようにします — 自動ロックを変えず、アプリもインストールせずに。iOS 16.4 以降の Safari と Chrome で動く無料ウェブツール。",
 keywords="iphone 画面 消えない, iphone 画面 つけたまま, iphone 自動ロック 防ぐ, ipad 画面 つけたまま, ios 画面 スリープさせない, iphone 画面 常時表示",
 ogtitle="iPhone の画面をスリープさせない方法 — 無料・アプリ不要",
 ogdesc="iPhone や iPad の画面を Safari からつけたままに。アプリ不要、自動ロックも変更不要。無料。",
 tag="iPhone・iPad", h1='iPhone の<span>画面をスリープさせない</span>方法',
 lead="iPhone や iPad の画面が消えないようにします — 自動ロックを変えず、アプリもインストールせずに。Safari で直接動作、無料。",
 body="""<p>レシピを読む、楽譜を追う、QR メニューを読み取る、スマホで資料を見る——iOS は<strong>自動ロック</strong>の時間が過ぎると画面を暗くしてロックします。毎回「設定」を開いてもいいですが、ScreenWakeUp を開けば、<strong>Screen Wake Lock API</strong>（iOS 16.4 以降）でタブが開いている間ずっと画面を点けたままにできます。</p>
  <div class="box"><strong>かんたん版:</strong> Safari で <a class="inline" href="{HOME}">screenwakeup.com</a> を開く → <strong>「画面をスリープさせない」</strong>をタップ → タブを表示したままに。完了。</div>
  <h2>3ステップで iPhone の画面を点けたままに</h2>
  <ol>
    <li>iPhone か iPad の <strong>Safari</strong> で <a class="inline" href="{HOME}">screenwakeup.com</a> を開きます。</li>
    <li>時間を選択 — 30分・1時間・2時間・4時間・∞。</li>
    <li><strong>「画面をスリープさせない」</strong>をタップし、Safari のタブを開いたまま表示しておきます。</li>
  </ol>
  <p>ヒント：ホーム画面に追加（共有 → ホーム画面に追加）すると、アプリのように開けます。</p>
  <h2>自動ロックを変えるだけではダメ？</h2>
  <p><em>設定 &gt; 画面表示と明るさ &gt; 自動ロック &gt; なし</em>に設定もできますが、それだと画面が<strong>一切</strong>ロックされず、バッテリーを消費し、一日中ロック解除のままになります。ScreenWakeUp は必要なときだけ画面を点け、タブを閉じれば元に戻ります。</p>
  <h2>必要なもの</h2>
  <ul>
    <li>Safari のネイティブ Wake Lock API には <strong>iOS / iPadOS 16.4 以降</strong>。</li>
    <li>タブは<strong>開いたまま表示</strong>しておく必要があります — 別アプリに切り替えたり端末をロックすると iOS がロックを解放し、戻ると再取得します。</li>
  </ul>
  <h2>よくある質問</h2>
  <h3>iPad でも使えますか？</h3>
  <p>はい、同じです — iPadOS の Safari か Chrome。レシピ・プレゼン・キオスク表示に最適です。</p>
  <h3>バッテリーを消費しますか？</h3>
  <p>どんな画面でも点けたままにすれば電力を使いますが、タブがアクティブな間だけです。閉じれば通常の自動ロックに戻るので、「なし」設定よりずっと安全です。</p>""",
 cta="iPhone を点けたままに → ツールを開く",
 related=[("Teams の退席中を防ぐ", "prevent-teams-away"), ("無料の Caffeine 代替", "caffeine-alternative")],
 bc_self="iPhone の画面をスリープさせない",
 howto=dict(name="iPhone の画面をスリープさせない方法",
            desc="自動ロックを変えず、アプリもインストールせずに、iPhone や iPad の画面を点けたままにします。",
            steps=[("Safari で開く", "iPhone か iPad の Safari で screenwakeup.com を開きます（iOS 16.4 以降）。"),
                   ("時間を選ぶ", "画面を点けておく時間、または ∞ を選びます。"),
                   ("「画面をスリープさせない」をタップ", "ボタンをタップし、Safari のタブを開いたまま表示しておきます。")]),
 faq=[("自動ロックを変えずに iPhone の画面を点けたままにするには？", "Safari で screenwakeup.com を開き、「画面をスリープさせない」をタップします。Screen Wake Lock API（iOS 16.4 以降）を使い、タブが開いている間は画面を点けたままにします。設定 > 画面表示と明るさ > 自動ロックを変える必要はありません。"),
      ("iPad でも使えますか？", "はい。iPadOS の Safari か Chrome で同じように動作します。タブを開いたまま表示しておいてください。"),
      ("どの iOS バージョンが必要ですか？", "iOS・iPadOS 16.4 以降が Safari の Screen Wake Lock API に対応しています。古いバージョンでは代替方式を使いますが、16.4 以降が最も安定します。"),
      ("端末をロックしたりアプリを切り替えると画面が暗くなるのはなぜ？", "ウェイクロックはタブが開いて表示されている間だけ有効です。別アプリに切り替えたり端末をロックすると iOS が解放します。タブに戻ると自動的に再有効化されます。")],
)
CONTENT["keep-screen-awake-iphone"]["ru"] = dict(
 title="Как не дать экрану iPhone гаснуть — Бесплатно, без приложения (iOS и iPad) | ScreenWakeUp",
 desc="Не дайте экрану iPhone или iPad выключаться — не меняя Автоблокировку и не устанавливая приложение. Бесплатный веб-инструмент для Safari и Chrome на iOS 16.4+.",
 keywords="экран iphone не гаснет, держать экран iphone включённым, отключить автоблокировку iphone, ipad экран активен, держать экран ios, экран iphone всегда включён",
 ogtitle="Как не дать экрану iPhone гаснуть — Бесплатно, без приложения",
 ogdesc="Держите экран iPhone или iPad включённым из Safari. Без приложения, без изменения Автоблокировки. Бесплатно.",
 tag="iPhone и iPad", h1='Как <span>не дать экрану iPhone гаснуть</span>',
 lead="Не дайте экрану iPhone или iPad выключаться — не меняя Автоблокировку и не устанавливая приложение. Работает прямо в Safari, бесплатно.",
 body="""<p>Читаете рецепт, следите за нотами, сканируете QR-меню или смотрите документ на телефоне? iOS гасит и блокирует экран по истечении времени <strong>Автоблокировки</strong>. Можно каждый раз лезть в Настройки — или открыть ScreenWakeUp, который через <strong>Screen Wake Lock API</strong> (iOS 16.4+) держит экран включённым, пока вкладка открыта.</p>
  <div class="box"><strong>Коротко:</strong> откройте <a class="inline" href="{HOME}">screenwakeup.com</a> в Safari → нажмите <strong>Держать экран активным</strong> → оставьте вкладку видимой. Готово.</div>
  <h2>Держите экран iPhone включённым за 3 шага</h2>
  <ol>
    <li>Откройте <a class="inline" href="{HOME}">screenwakeup.com</a> в <strong>Safari</strong> на iPhone или iPad.</li>
    <li>Выберите длительность — 30 мин, 1 ч, 2 ч, 4 ч или ∞.</li>
    <li>Нажмите <strong>Держать экран активным</strong> и оставьте вкладку Safari открытой и на экране.</li>
  </ol>
  <p>Совет: добавьте на экран «Домой» (Поделиться → На экран «Домой»), чтобы открывать как приложение.</p>
  <h2>Почему не просто изменить Автоблокировку?</h2>
  <p>Можно поставить <em>Настройки &gt; Экран и яркость &gt; Автоблокировка &gt; Никогда</em> — но тогда экран <strong>никогда</strong> не блокируется, садит батарею и оставляет телефон разблокированным весь день. ScreenWakeUp держит экран включённым только когда нужно; закрыли вкладку — всё вернулось к норме.</p>
  <h2>Что нужно</h2>
  <ul>
    <li><strong>iOS / iPadOS 16.4 или новее</strong> для нативного Wake Lock API в Safari.</li>
    <li>Вкладка должна оставаться <strong>открытой и видимой</strong> — если переключиться на другое приложение или заблокировать телефон, iOS освобождает блокировку и восстанавливает её при возврате.</li>
  </ul>
  <h2>Частые вопросы</h2>
  <h3>Работает ли на iPad?</h3>
  <p>Да, так же — Safari или Chrome на iPadOS. Отлично для рецептов, презентаций и экранов-витрин.</p>
  <h3>Сажает ли батарею?</h3>
  <p>Любой включённый экран расходует энергию, но только пока вкладка активна. Закроете её — вернётся обычная Автоблокировка, что намного безопаснее режима «Никогда».</p>""",
 cta="Держите iPhone включённым → откройте инструмент",
 related=[("Избежать статуса «Нет на месте» в Teams", "prevent-teams-away"), ("Бесплатная замена Caffeine", "caffeine-alternative")],
 bc_self="Держать экран iPhone активным",
 howto=dict(name="Как не дать экрану iPhone гаснуть",
            desc="Держите экран iPhone или iPad включённым, не меняя Автоблокировку и не устанавливая приложение.",
            steps=[("Откройте в Safari", "Откройте screenwakeup.com в Safari на iPhone или iPad (iOS 16.4 или новее)."),
                   ("Выберите длительность", "Выберите, как долго экран должен оставаться включённым, или ∞."),
                   ("Нажмите «Держать экран активным»", "Нажмите кнопку и оставьте вкладку Safari открытой и видимой.")]),
 faq=[("Как держать экран iPhone включённым, не меняя Автоблокировку?", "Откройте screenwakeup.com в Safari и нажмите «Держать экран активным». Он использует Screen Wake Lock API (iOS 16.4+), чтобы держать экран включённым, пока вкладка открыта, без изменения Настройки > Экран и яркость > Автоблокировка."),
      ("Работает ли на iPad?", "Да. Работает так же на iPadOS в Safari или Chrome. Держите вкладку открытой и на экране."),
      ("Какая версия iOS нужна?", "iOS и iPadOS 16.4 или новее поддерживают Screen Wake Lock API в Safari. На старых версиях используется запасной метод, но надёжнее всего на 16.4+."),
      ("Почему экран всё равно гаснет, когда я блокирую телефон или переключаю приложение?", "Блокировка экрана действует, только пока вкладка открыта и видима. Если переключиться на другое приложение или заблокировать телефон, iOS освобождает её. Вернитесь на вкладку — она активируется снова.")],
)
