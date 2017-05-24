import sound.formats.wavread
import sound.formats.wavwrite

import sound.formats.aiffread
import sound.formats.aiffwrite
import sound.formats.auread
import sound.formats.auwrite

import sound.effects.echo
import sound.effects.surround
import sound.effects.reverse

import sound.filters.equalizer
import sound.filters.vocoder
import sound.filters.karaoke

sound.formats.wavread.wav_read()
sound.formats.wavwrite.wav_write()
print()

sound.formats.aiffread.aiff_read()
sound.formats.aiffwrite.aiff_write()
print()

sound.formats.auread.au_read()
sound.formats.auwrite.au_write()
print()

sound.effects.echo.effect_echo()
sound.effects.surround.effect_surround()
sound.effects.reverse.effect_reverse()
print()

sound.filters.equalizer.filter_equalizer()
sound.filters.vocoder.filter_vocoder()
sound.filters.karaoke.filter_karaoke()
print()
