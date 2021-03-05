// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flyteidl/plugins/presto.proto

#include "flyteidl/plugins/presto.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

namespace flyteidl {
namespace plugins {
class PrestoQueryDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<PrestoQuery> _instance;
} _PrestoQuery_default_instance_;
}  // namespace plugins
}  // namespace flyteidl
static void InitDefaultsPrestoQuery_flyteidl_2fplugins_2fpresto_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::flyteidl::plugins::_PrestoQuery_default_instance_;
    new (ptr) ::flyteidl::plugins::PrestoQuery();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::flyteidl::plugins::PrestoQuery::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<0> scc_info_PrestoQuery_flyteidl_2fplugins_2fpresto_2eproto =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 0, InitDefaultsPrestoQuery_flyteidl_2fplugins_2fpresto_2eproto}, {}};

void InitDefaults_flyteidl_2fplugins_2fpresto_2eproto() {
  ::google::protobuf::internal::InitSCC(&scc_info_PrestoQuery_flyteidl_2fplugins_2fpresto_2eproto.base);
}

::google::protobuf::Metadata file_level_metadata_flyteidl_2fplugins_2fpresto_2eproto[1];
constexpr ::google::protobuf::EnumDescriptor const** file_level_enum_descriptors_flyteidl_2fplugins_2fpresto_2eproto = nullptr;
constexpr ::google::protobuf::ServiceDescriptor const** file_level_service_descriptors_flyteidl_2fplugins_2fpresto_2eproto = nullptr;

const ::google::protobuf::uint32 TableStruct_flyteidl_2fplugins_2fpresto_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::PrestoQuery, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::PrestoQuery, routing_group_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::PrestoQuery, catalog_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::PrestoQuery, schema_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::PrestoQuery, statement_),
};
static const ::google::protobuf::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::flyteidl::plugins::PrestoQuery)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::flyteidl::plugins::_PrestoQuery_default_instance_),
};

::google::protobuf::internal::AssignDescriptorsTable assign_descriptors_table_flyteidl_2fplugins_2fpresto_2eproto = {
  {}, AddDescriptors_flyteidl_2fplugins_2fpresto_2eproto, "flyteidl/plugins/presto.proto", schemas,
  file_default_instances, TableStruct_flyteidl_2fplugins_2fpresto_2eproto::offsets,
  file_level_metadata_flyteidl_2fplugins_2fpresto_2eproto, 1, file_level_enum_descriptors_flyteidl_2fplugins_2fpresto_2eproto, file_level_service_descriptors_flyteidl_2fplugins_2fpresto_2eproto,
};

const char descriptor_table_protodef_flyteidl_2fplugins_2fpresto_2eproto[] =
  "\n\035flyteidl/plugins/presto.proto\022\020flyteid"
  "l.plugins\032\031flyteidl/core/tasks.proto\"X\n\013"
  "PrestoQuery\022\025\n\rrouting_group\030\001 \001(\t\022\017\n\007ca"
  "talog\030\002 \001(\t\022\016\n\006schema\030\003 \001(\t\022\021\n\tstatement"
  "\030\004 \001(\tB9Z7github.com/flyteorg/flyteidl/g"
  "en/pb-go/flyteidl/pluginsb\006proto3"
  ;
::google::protobuf::internal::DescriptorTable descriptor_table_flyteidl_2fplugins_2fpresto_2eproto = {
  false, InitDefaults_flyteidl_2fplugins_2fpresto_2eproto, 
  descriptor_table_protodef_flyteidl_2fplugins_2fpresto_2eproto,
  "flyteidl/plugins/presto.proto", &assign_descriptors_table_flyteidl_2fplugins_2fpresto_2eproto, 233,
};

void AddDescriptors_flyteidl_2fplugins_2fpresto_2eproto() {
  static constexpr ::google::protobuf::internal::InitFunc deps[1] =
  {
    ::AddDescriptors_flyteidl_2fcore_2ftasks_2eproto,
  };
 ::google::protobuf::internal::AddDescriptors(&descriptor_table_flyteidl_2fplugins_2fpresto_2eproto, deps, 1);
}

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_flyteidl_2fplugins_2fpresto_2eproto = []() { AddDescriptors_flyteidl_2fplugins_2fpresto_2eproto(); return true; }();
namespace flyteidl {
namespace plugins {

// ===================================================================

void PrestoQuery::InitAsDefaultInstance() {
}
class PrestoQuery::HasBitSetters {
 public:
};

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int PrestoQuery::kRoutingGroupFieldNumber;
const int PrestoQuery::kCatalogFieldNumber;
const int PrestoQuery::kSchemaFieldNumber;
const int PrestoQuery::kStatementFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

PrestoQuery::PrestoQuery()
  : ::google::protobuf::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:flyteidl.plugins.PrestoQuery)
}
PrestoQuery::PrestoQuery(const PrestoQuery& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  routing_group_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.routing_group().size() > 0) {
    routing_group_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.routing_group_);
  }
  catalog_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.catalog().size() > 0) {
    catalog_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.catalog_);
  }
  schema_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.schema().size() > 0) {
    schema_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.schema_);
  }
  statement_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.statement().size() > 0) {
    statement_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.statement_);
  }
  // @@protoc_insertion_point(copy_constructor:flyteidl.plugins.PrestoQuery)
}

void PrestoQuery::SharedCtor() {
  ::google::protobuf::internal::InitSCC(
      &scc_info_PrestoQuery_flyteidl_2fplugins_2fpresto_2eproto.base);
  routing_group_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  catalog_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  schema_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  statement_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

PrestoQuery::~PrestoQuery() {
  // @@protoc_insertion_point(destructor:flyteidl.plugins.PrestoQuery)
  SharedDtor();
}

void PrestoQuery::SharedDtor() {
  routing_group_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  catalog_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  schema_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  statement_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

void PrestoQuery::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const PrestoQuery& PrestoQuery::default_instance() {
  ::google::protobuf::internal::InitSCC(&::scc_info_PrestoQuery_flyteidl_2fplugins_2fpresto_2eproto.base);
  return *internal_default_instance();
}


void PrestoQuery::Clear() {
// @@protoc_insertion_point(message_clear_start:flyteidl.plugins.PrestoQuery)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  routing_group_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  catalog_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  schema_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  statement_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  _internal_metadata_.Clear();
}

#if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
const char* PrestoQuery::_InternalParse(const char* begin, const char* end, void* object,
                  ::google::protobuf::internal::ParseContext* ctx) {
  auto msg = static_cast<PrestoQuery*>(object);
  ::google::protobuf::int32 size; (void)size;
  int depth; (void)depth;
  ::google::protobuf::uint32 tag;
  ::google::protobuf::internal::ParseFunc parser_till_end; (void)parser_till_end;
  auto ptr = begin;
  while (ptr < end) {
    ptr = ::google::protobuf::io::Parse32(ptr, &tag);
    GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
    switch (tag >> 3) {
      // string routing_group = 1;
      case 1: {
        if (static_cast<::google::protobuf::uint8>(tag) != 10) goto handle_unusual;
        ptr = ::google::protobuf::io::ReadSize(ptr, &size);
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        ctx->extra_parse_data().SetFieldName("flyteidl.plugins.PrestoQuery.routing_group");
        object = msg->mutable_routing_group();
        if (size > end - ptr + ::google::protobuf::internal::ParseContext::kSlopBytes) {
          parser_till_end = ::google::protobuf::internal::GreedyStringParserUTF8;
          goto string_till_end;
        }
        GOOGLE_PROTOBUF_PARSER_ASSERT(::google::protobuf::internal::StringCheckUTF8(ptr, size, ctx));
        ::google::protobuf::internal::InlineGreedyStringParser(object, ptr, size, ctx);
        ptr += size;
        break;
      }
      // string catalog = 2;
      case 2: {
        if (static_cast<::google::protobuf::uint8>(tag) != 18) goto handle_unusual;
        ptr = ::google::protobuf::io::ReadSize(ptr, &size);
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        ctx->extra_parse_data().SetFieldName("flyteidl.plugins.PrestoQuery.catalog");
        object = msg->mutable_catalog();
        if (size > end - ptr + ::google::protobuf::internal::ParseContext::kSlopBytes) {
          parser_till_end = ::google::protobuf::internal::GreedyStringParserUTF8;
          goto string_till_end;
        }
        GOOGLE_PROTOBUF_PARSER_ASSERT(::google::protobuf::internal::StringCheckUTF8(ptr, size, ctx));
        ::google::protobuf::internal::InlineGreedyStringParser(object, ptr, size, ctx);
        ptr += size;
        break;
      }
      // string schema = 3;
      case 3: {
        if (static_cast<::google::protobuf::uint8>(tag) != 26) goto handle_unusual;
        ptr = ::google::protobuf::io::ReadSize(ptr, &size);
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        ctx->extra_parse_data().SetFieldName("flyteidl.plugins.PrestoQuery.schema");
        object = msg->mutable_schema();
        if (size > end - ptr + ::google::protobuf::internal::ParseContext::kSlopBytes) {
          parser_till_end = ::google::protobuf::internal::GreedyStringParserUTF8;
          goto string_till_end;
        }
        GOOGLE_PROTOBUF_PARSER_ASSERT(::google::protobuf::internal::StringCheckUTF8(ptr, size, ctx));
        ::google::protobuf::internal::InlineGreedyStringParser(object, ptr, size, ctx);
        ptr += size;
        break;
      }
      // string statement = 4;
      case 4: {
        if (static_cast<::google::protobuf::uint8>(tag) != 34) goto handle_unusual;
        ptr = ::google::protobuf::io::ReadSize(ptr, &size);
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        ctx->extra_parse_data().SetFieldName("flyteidl.plugins.PrestoQuery.statement");
        object = msg->mutable_statement();
        if (size > end - ptr + ::google::protobuf::internal::ParseContext::kSlopBytes) {
          parser_till_end = ::google::protobuf::internal::GreedyStringParserUTF8;
          goto string_till_end;
        }
        GOOGLE_PROTOBUF_PARSER_ASSERT(::google::protobuf::internal::StringCheckUTF8(ptr, size, ctx));
        ::google::protobuf::internal::InlineGreedyStringParser(object, ptr, size, ctx);
        ptr += size;
        break;
      }
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->EndGroup(tag);
          return ptr;
        }
        auto res = UnknownFieldParse(tag, {_InternalParse, msg},
          ptr, end, msg->_internal_metadata_.mutable_unknown_fields(), ctx);
        ptr = res.first;
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr != nullptr);
        if (res.second) return ptr;
      }
    }  // switch
  }  // while
  return ptr;
string_till_end:
  static_cast<::std::string*>(object)->clear();
  static_cast<::std::string*>(object)->reserve(size);
  goto len_delim_till_end;
len_delim_till_end:
  return ctx->StoreAndTailCall(ptr, end, {_InternalParse, msg},
                               {parser_till_end, object}, size);
}
#else  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
bool PrestoQuery::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!PROTOBUF_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:flyteidl.plugins.PrestoQuery)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // string routing_group = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (10 & 0xFF)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_routing_group()));
          DO_(::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
            this->routing_group().data(), static_cast<int>(this->routing_group().length()),
            ::google::protobuf::internal::WireFormatLite::PARSE,
            "flyteidl.plugins.PrestoQuery.routing_group"));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // string catalog = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (18 & 0xFF)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_catalog()));
          DO_(::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
            this->catalog().data(), static_cast<int>(this->catalog().length()),
            ::google::protobuf::internal::WireFormatLite::PARSE,
            "flyteidl.plugins.PrestoQuery.catalog"));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // string schema = 3;
      case 3: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (26 & 0xFF)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_schema()));
          DO_(::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
            this->schema().data(), static_cast<int>(this->schema().length()),
            ::google::protobuf::internal::WireFormatLite::PARSE,
            "flyteidl.plugins.PrestoQuery.schema"));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // string statement = 4;
      case 4: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (34 & 0xFF)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_statement()));
          DO_(::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
            this->statement().data(), static_cast<int>(this->statement().length()),
            ::google::protobuf::internal::WireFormatLite::PARSE,
            "flyteidl.plugins.PrestoQuery.statement"));
        } else {
          goto handle_unusual;
        }
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, _internal_metadata_.mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:flyteidl.plugins.PrestoQuery)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:flyteidl.plugins.PrestoQuery)
  return false;
#undef DO_
}
#endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER

void PrestoQuery::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:flyteidl.plugins.PrestoQuery)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // string routing_group = 1;
  if (this->routing_group().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->routing_group().data(), static_cast<int>(this->routing_group().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.routing_group");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      1, this->routing_group(), output);
  }

  // string catalog = 2;
  if (this->catalog().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->catalog().data(), static_cast<int>(this->catalog().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.catalog");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      2, this->catalog(), output);
  }

  // string schema = 3;
  if (this->schema().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->schema().data(), static_cast<int>(this->schema().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.schema");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      3, this->schema(), output);
  }

  // string statement = 4;
  if (this->statement().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->statement().data(), static_cast<int>(this->statement().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.statement");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      4, this->statement(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:flyteidl.plugins.PrestoQuery)
}

::google::protobuf::uint8* PrestoQuery::InternalSerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:flyteidl.plugins.PrestoQuery)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // string routing_group = 1;
  if (this->routing_group().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->routing_group().data(), static_cast<int>(this->routing_group().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.routing_group");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        1, this->routing_group(), target);
  }

  // string catalog = 2;
  if (this->catalog().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->catalog().data(), static_cast<int>(this->catalog().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.catalog");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        2, this->catalog(), target);
  }

  // string schema = 3;
  if (this->schema().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->schema().data(), static_cast<int>(this->schema().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.schema");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        3, this->schema(), target);
  }

  // string statement = 4;
  if (this->statement().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->statement().data(), static_cast<int>(this->statement().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.PrestoQuery.statement");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        4, this->statement(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flyteidl.plugins.PrestoQuery)
  return target;
}

size_t PrestoQuery::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flyteidl.plugins.PrestoQuery)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // string routing_group = 1;
  if (this->routing_group().size() > 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->routing_group());
  }

  // string catalog = 2;
  if (this->catalog().size() > 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->catalog());
  }

  // string schema = 3;
  if (this->schema().size() > 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->schema());
  }

  // string statement = 4;
  if (this->statement().size() > 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->statement());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void PrestoQuery::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:flyteidl.plugins.PrestoQuery)
  GOOGLE_DCHECK_NE(&from, this);
  const PrestoQuery* source =
      ::google::protobuf::DynamicCastToGenerated<PrestoQuery>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:flyteidl.plugins.PrestoQuery)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:flyteidl.plugins.PrestoQuery)
    MergeFrom(*source);
  }
}

void PrestoQuery::MergeFrom(const PrestoQuery& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flyteidl.plugins.PrestoQuery)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.routing_group().size() > 0) {

    routing_group_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.routing_group_);
  }
  if (from.catalog().size() > 0) {

    catalog_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.catalog_);
  }
  if (from.schema().size() > 0) {

    schema_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.schema_);
  }
  if (from.statement().size() > 0) {

    statement_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.statement_);
  }
}

void PrestoQuery::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:flyteidl.plugins.PrestoQuery)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void PrestoQuery::CopyFrom(const PrestoQuery& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flyteidl.plugins.PrestoQuery)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool PrestoQuery::IsInitialized() const {
  return true;
}

void PrestoQuery::Swap(PrestoQuery* other) {
  if (other == this) return;
  InternalSwap(other);
}
void PrestoQuery::InternalSwap(PrestoQuery* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  routing_group_.Swap(&other->routing_group_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  catalog_.Swap(&other->catalog_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  schema_.Swap(&other->schema_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  statement_.Swap(&other->statement_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
}

::google::protobuf::Metadata PrestoQuery::GetMetadata() const {
  ::google::protobuf::internal::AssignDescriptors(&::assign_descriptors_table_flyteidl_2fplugins_2fpresto_2eproto);
  return ::file_level_metadata_flyteidl_2fplugins_2fpresto_2eproto[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace plugins
}  // namespace flyteidl
namespace google {
namespace protobuf {
template<> PROTOBUF_NOINLINE ::flyteidl::plugins::PrestoQuery* Arena::CreateMaybeMessage< ::flyteidl::plugins::PrestoQuery >(Arena* arena) {
  return Arena::CreateInternal< ::flyteidl::plugins::PrestoQuery >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
