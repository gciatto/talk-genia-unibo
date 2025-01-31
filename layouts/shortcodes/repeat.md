{{ $min := cast.ToInt (.Get "minInclusive" | default "0") }}
{{ $max := cast.ToInt (.Get "maxExclusive" | default "1") }}
{{ $content := .Inner }}
{{ $split := strings.Split $content "[-content-]" }}
{{ $header := index $split 0 }}
{{ $content := index $split 1 }}
{{ range seq $min $max }}
{{ strings.Replace $header "[-index-]" (cast.ToString .) | markdownify }}
{{ strings.Replace $content "[-index-]" (cast.ToString .) | markdownify}}
{{ if ne . $max }}
---
{{ end }}
{{ end }}
