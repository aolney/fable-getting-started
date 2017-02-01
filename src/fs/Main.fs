module App.Main

open Fable.Import
open App.Message

// This must be before everything else
Fable.Core.JsInterop.importAll "core-js"

let main () =
    Browser.console.log message

do
    main ()
