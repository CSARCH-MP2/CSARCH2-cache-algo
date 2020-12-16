from cache_alg.tag_block_word import TagBlockWord

lines = open('./inputs/tagblockword_input.txt', 'r').read().splitlines()
mm_blocks = int(lines[0].split(' ')[1])
wordsperblock = int(lines[1].split(' ')[1])
bitsperword = int(lines[2].split(' ')[1])
c_blocks = int(lines[3].split(' ')[1])

tbw = TagBlockWord(
  n_cache_blocks=c_blocks,
  n_words_per_block=wordsperblock,
  n_bits_per_word=bitsperword,
  n_mem_words=mm_blocks * wordsperblock)

tbw.print_id()
